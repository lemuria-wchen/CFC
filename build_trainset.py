# this script is used to build train set for contrastive learning in retrieval-based dialogue system

import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import numpy as np
from collections import defaultdict
import json


seed = 12345
np.random.seed(seed)

min_num_ctxs, max_num_ctxs = 4, 50

# assign each unique response a id
prefix = '/home/v-wchen2/data/reddit'
fin_path = os.path.join(prefix, 'train_cr.tsv')

db = []
var = defaultdict(int)

with open(fin_path, 'r', encoding='utf-8') as f:
    for line in tqdm(f):
        ctx, rsp = line.strip().split('\t')
        var[rsp] = var.get(rsp) if rsp in var else len(var)
        db.append({'ctx': ctx, 'rsp': rsp, 'rid': var[rsp]})

db = np.array(db)

# get response ids with single & multiple contexts
rc, rmc = defaultdict(list), defaultdict(list)

for idx, sample in tqdm(enumerate(db)):
    rc[sample.get('rid')].append(idx)

for rid, idxs in tqdm(rc.items()):
    if min_num_ctxs <= len(idxs) <= max_num_ctxs:
        rmc[rid] = idxs


# random choose two contexts (same response) as positive sample
train = []

for rid, idxs in tqdm(rmc.items()):
    samples = [db[idx] for idx in idxs]
    ctxs = [sample['ctx'] for sample in samples]
    rsp = samples[0]['rsp']
    train.append({
        'ctxs': ctxs,
        'info': {'rsp': rsp, 'rid': rid, 'idxs': idxs}
    })


def write_to_json(obj, json_path):
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(obj, file, ensure_ascii=False, indent=4)


train, dev = train_test_split(train, test_size=0.1, random_state=seed)

# save train/dev set
write_to_json(train, os.path.join(prefix, 'train.json'))
write_to_json(dev, os.path.join(prefix, 'dev.json'))
