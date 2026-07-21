# Budget-sweep interpretation

- Set A: Avg Risk@B 最优为 **GraphSAGE-TEG-Gate**；CVaR90/CVaR95 AUBRC 最优分别为 **GraphSAGE-TEG-Gate** / **GraphSAGE-TEG-Gate**。
- Set B: Avg Risk@B 最优为 **SGFormer-TEG-Gate**；CVaR90/CVaR95 AUBRC 最优分别为 **SGFormer-TEG-Gate** / **GraphSAGE-TEG-Gate**。
- A/B 平均：Avg Risk@B、CVaR90 AUBRC、CVaR95 AUBRC 最优分别为 **GraphSAGE-TEG-Gate**、**SGFormer-TEG-Gate**、**GraphSAGE-TEG-Gate**。
- Stable-Tail GNN 的综合核心风险 mean-rank 为 2.333，排序第 3（共 13 个模型），因此本次扫描不支持其在所有模型中‘总风险 + 尾部风险综合最稳’的强表述；但它仍是主表模型中 CVaR95 AUBRC 最低的模型。
- SGFormer-TEG-Gate 在 Set B、A/B 平均 CVaR90 或 LoadCVaR 上优于 Stable-Tail GNN，但 Stable-Tail GNN 的 A/B 平均 CVaR95 与 MaxVehCVaR90 更低；因此将前者定位为强主干扩展模型，而不是直接替代 Stable-Tail GNN 的论文主模型。
