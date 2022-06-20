# CFC
Code and created datasets for our ACL 2022 paper: [Contextual Fine-to-Coarse Distillation for Coarse-grained Response Selection in Open-Domain Conversations](https://aclanthology.org/2022.acl-long.334/).

### TODO

- make code available

### Dataset

We created two datasets in the paper, `Reddit` and `Twitter`, and their statistics and interpretations are shown in the table below.

<table>
<thead>
  <tr>
    <th rowspan="2">Datasets</th>
    <th rowspan="2">Train set</th>
    <th rowspan="2">Dev set</th>
    <th colspan="2">Test set</th>
    <th rowspan="2">Database</th>
  </tr>
  <tr>
    <th>MC</th>
    <th>SC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Reddit</td>
    <td>300K</td>
    <td>20K</td>
    <td>20K</td>
    <td>20K</td>
    <td>10M</td>
  </tr>
  <tr>
    <td>Twitter</td>
    <td>20K</td>
    <td>2K</td>
    <td>2K</td>
    <td>-</td>
    <td>1M</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th rowspan="2">File</th>
    <th rowspan="2">Role</th>
    <th rowspan="2">Explanation</th>
  </tr>
  <tr>
  </tr>
</thead>
<tbody>
  <tr>
    <td>train.json</td>
    <td>Train set</td>
    <td>Each instance contains a response and a context list corresponding to the response.</td>
  </tr>
  <tr>
    <td>dev.json</td>
    <td>Dev set</td>
    <td>Same as training set.</td>
  </tr>
  <tr>
    <td>test_mc.json</td>
    <td>MC test set</td>
    <td>Same as database. Each response in MC test set has multiple contexts, which ensures that there exists other contexts in the database that also correspond to this response.</td>
  </tr>
  <tr>
    <td>test_sc.json</td>
    <td>SC test set</td>
    <td>Same as database. Each response in SC test set has only one context, i.e., there is no context in the database that exactly corresponds to the response.</td>
  </tr>
</tbody>
</table>


### Dataset Setup

Instead of providing the data directly, we provide a script to make the data in consideration of copyright issues. 

To download raw reddit dataset `train.tsv`, following [https://github.com/microsoft/DialoGPT](https://github.com/microsoft/DialoGPT) and run `python demo.py --data full`. Raw twitter dataset is available in [https://github.com/Marsan-Ma-zz/chat_corpus](https://github.com/Marsan-Ma-zz/chat_corpus).  

- build context-response pairs

```shell
python build_data.py
```

- build training set

```shell
python build_trainset.py
```

- build test set

```shell
python build_testset.py
```
