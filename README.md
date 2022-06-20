# CFC
Code and created datasets for our ACL 2022 paper: [Contextual Fine-to-Coarse Distillation for Coarse-grained Response Selection in Open-Domain Conversations](https://aclanthology.org/2022.acl-long.334/).

### News

- Reddit and Twitter datasets released ! (2022.06.20)

### TODO

- The codes will be released in the near future.

### Dataset

We created two datasets in the [paper](https://aclanthology.org/2022.acl-long.334/) for contextual matching, i.e., `Reddit` and `Twitter`, and the statistics and interpretations are shown in the table below.

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
    <th rowspan="2">Explaination</th>
  </tr>
  <tr>
  </tr>
</thead>
<tbody>
  <tr>
    <td>database.json</td>
    <td>Database</td>
    <td>Each instance contains three fields, where `ctx` represents the context, `rsp` represents the response, and   `rid` represents the ID of the response.</td>
  </tr>
  <tr>
    <td>train.json</td>
    <td>Trainset</td>
    <td>Each instance contains a&nbsp;&nbsp;&nbsp;response and a context list corresponding to the response.</td>
  </tr>
  <tr>
    <td>dev.json</td>
    <td>Devset</td>
    <td>Same as training set.</td>
  </tr>
  <tr>
    <td>test_mc.json</td>
    <td>MC testset</td>
    <td>Same as database. Each response in MC test set has multiple contexts, which ensures that there exits other contexts in the database that also correspond to this response.</td>
  </tr>
  <tr>
    <td>test_sc.json</td>
    <td>SC testset</td>
    <td>Same as database. Each response in SC test set has only one context, i.e., there is no context in the database that exactly corresponds to the response.</td>
  </tr>
</tbody>
</table>

### Build Dataset

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

### How to Cite

If you extend or use this work, please cite the [paper](https://aclanthology.org/2022.acl-long.334/) where it was introduced:

```shell
@inproceedings{chen-etal-2022-contextual,
    title = "Contextual Fine-to-Coarse Distillation for Coarse-grained Response Selection in Open-Domain Conversations",
    author = "Chen, Wei and Gong, Yeyun and Xu, Can and Hu, Huang and Yao, Bolun and Wei, Zhongyu and Fan, Zhihao and Hu, Xiaowu and Zhou, Bartuer and Cheng, Biao and Jiang, Daxin and Duan, Nan",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.334",
    doi = "10.18653/v1/2022.acl-long.334",
    pages = "4865--4877",
    abstract = "We study the problem of coarse-grained response selection in retrieval-based dialogue systems. The problem is equally important with fine-grained response selection, but is less explored in existing literature. In this paper, we propose a Contextual Fine-to-Coarse (CFC) distilled model for coarse-grained response selection in open-domain conversations. In our CFC model, dense representations of query, candidate contexts and responses is learned based on the multi-tower architecture using contextual matching, and richer knowledge learned from the one-tower architecture (fine-grained) is distilled into the multi-tower architecture (coarse-grained) to enhance the performance of the retriever. To evaluate the performance of the proposed model, we construct two new datasets based on the Reddit comments dump and Twitter corpus. Extensive experimental results on the two datasets show that the proposed method achieves huge improvement over all evaluation metrics compared with traditional baseline methods.",
}
```
