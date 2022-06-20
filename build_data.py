# this script is used to split train set & test set / database in retrieval-based dialogue system
import os

from tqdm import tqdm
import numpy as np
from sklearn.model_selection import train_test_split


seed = 12345  # random seed
np.random.seed(seed)

test_size = 0.2  # test set ratio

min_ctx_tokens, max_ctx_tokens = 5, 64
min_rsp_tokens, max_rsp_tokens = 5, 64


# step 1: download raw reddit dataset `train.tsv`
# follow https://github.com/microsoft/DialoGPT and run `python demo.py --data full`

# step 2: write all context-pairs in raw reddit dataset to `cr.tsv`
prefix = '/home/v-wchen2/data/reddit'

fin_path = os.path.join(prefix, 'train.tsv')
fout_path = os.path.join(prefix, 'cr.tsv')

if not os.path.exists(fout_path):
    with open(fin_path, 'r', encoding='utf-8') as fin:
        with open(fout_path, 'w', encoding='utf-8') as fout:
            for line in tqdm(fin):
                # split each line to a complete dialog
                _, ctxs, rsp = line.strip().split('\t')
                ctxs = [' '.join(ctx.strip().split()[1:]) for ctx in ctxs.split('EOS')]
                rsp = ' '.join(rsp.split()[1:])
                dialog = ctxs + [rsp]
                # given a complete dialog {x_1, x_2, ..., x_t}
                # for each i, use x_i as key and {x_1, x_2, ..., x_{i-1}} as value.
                t = len(dialog)
                for i in range(1, t):
                    rsp = dialog[i]
                    ctxs = ' [SEP] '.join(dialog[:i])
                    if min_ctx_tokens <= len(ctxs.split()) <= max_ctx_tokens and \
                            min_rsp_tokens <= len(rsp.split()) <= max_rsp_tokens:
                        fout.write(ctxs + '\t' + rsp + '\n')


# step 3: sampling and remove duplicate and split to train/test
fin_path = fout_path
fout_train_path = os.path.join(prefix, 'train_cr.tsv')
fout_test_path = os.path.join(prefix, 'test_cr.tsv')


if not os.path.exists(fout_train_path) or not os.path.exists(fout_test_path):
    lines = set()
    with open(fin_path, 'r', encoding='utf-8') as fin:
        for line in tqdm(fin):
            lines.add(line)

    train_cr, test_cr = train_test_split(list(lines), test_size=test_size, random_state=seed)

    fout_train_path = os.path.join(prefix, 'train_cr.tsv')
    with open(fout_train_path, 'w', encoding='utf-8') as fout:
        for line in tqdm(train_cr):
            fout.write(line)

    fout_test_path = os.path.join(prefix, 'test_cr.tsv')
    with open(fout_test_path, 'w', encoding='utf-8') as fout:
        for line in tqdm(test_cr):
            fout.write(line)
