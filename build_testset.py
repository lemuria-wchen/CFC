# this script is used to build testset and database in retrieval-based dialogue system
import os
from tqdm import tqdm
import numpy as np
from collections import defaultdict
import json


seed = 12345
np.random.seed(seed)

min_num_ctxs, max_num_ctxs = 4, 50
sc_size, mc_size, db_size = 20000, 20000, [1000000, 2000000, 5000000, 10000000]


# assign each unique response a id
prefix = '/home/v-wchen2/data/reddit'
fin_path = os.path.join(prefix, 'test_cr.tsv')

db = []
var = defaultdict(int)

with open(fin_path, 'r', encoding='utf-8') as f:
    for line in tqdm(f):
        ctx, rsp = line.strip().split('\t')
        var[rsp] = var.get(rsp) if rsp in var else len(var)
        db.append({'ctx': ctx, 'rsp': rsp, 'rid': var[rsp]})

db = np.array(db)

# get response ids with single & multiple contexts
rc, rsc, rmc = defaultdict(list), defaultdict(list), defaultdict(list)

for idx, sample in tqdm(enumerate(db)):
    rc[sample.get('rid')].append(idx)

for rid, idxs in tqdm(rc.items()):
    if len(idxs) == 1:
        rsc[rid] = idxs[0]
    else:
        rmc[rid] = idxs

# get eligible index list
sc_indices, mc_indices, mcr_indices = list(rsc.values()), [], []

for rid, idxs in rmc.items():
    _idxs = idxs[:]
    if min_num_ctxs <= len(_idxs) <= max_num_ctxs:
        # random choose a index
        mc_indices.append(_idxs.pop(np.random.choice(len(_idxs))))
        mcr_indices.append(_idxs)

mc_indices, mcr_indices = np.array(mc_indices), np.array(mcr_indices, dtype=object)

# create database and testset
if sc_size > len(sc_indices):
    print('too few eligible single context indices ({} < {})'.format(sc_size, len(sc_indices)))
    sc_size = len(sc_indices)

if mc_size > len(mc_indices):
    print('too few eligible multiple context indices ({} < {})'.format(mc_size, len(mc_indices)))
    mc_size = len(mc_indices)

sc_indices = np.random.choice(sc_indices, size=sc_size, replace=False)    # single context test index
_indices = np.random.choice(np.arange(len(mc_indices)), size=mc_size, replace=False)
mc_indices, mcr_indices = mc_indices[_indices], mcr_indices[_indices]    # multiple contexts test index
mcr_indices_flat = np.array([idx for indices in mcr_indices for idx in indices])


# save database and testset
def save_to_json(samples, path):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(samples, fout, ensure_ascii=False, indent=4)


test_sc, test_mc = list(db[sc_indices]), list(db[mc_indices])

save_to_json(test_sc, os.path.join(prefix, 'test_sc.json'))
save_to_json(test_mc, os.path.join(prefix, 'test_mc.json'))

for ds in db_size:
    db_indices = np.delete(np.arange(len(db)), np.concatenate([sc_indices, mc_indices, mcr_indices_flat]))
    db_indices = np.random.choice(db_indices, size=ds - len(mcr_indices_flat), replace=False)
    # mix other contexts in multi-contexts test set
    db_indices = np.concatenate([mcr_indices_flat, db_indices])     # database index
    candidate = list(db[db_indices])
    save_to_json(candidate, os.path.join(prefix, 'database_{}m.json'.format(int(ds / 1000000))))
