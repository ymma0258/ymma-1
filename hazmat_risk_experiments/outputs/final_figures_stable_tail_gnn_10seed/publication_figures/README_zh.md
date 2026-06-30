# 论文图表规划与说明（正式 10-seed 数据）

本图组只读取正式 10-seed 结果，不使用旧 5-seed 或探索性输出。统一采用色盲友好配色、白底、简化边框，并同时导出 600 dpi PNG、可编辑 SVG 和矢量 PDF。

## 图 1：总体研究框架

- 文件：`fig01_research_framework.*`
- 内容：2020/2021 轨迹图数据 → Stable-Tail GNN 节点风险学习 → 连续边风险矩阵 → OD 路径验证与 PyVRP-CVRP 下游验证 → 风险负担集中度后验评价 → 成本—风险—公平性决策。
- 目的：在方法章节开头交代论文主线，并明确 PyVRP 是下游求解器，而不是风险公平约束优化器。
- 图注建议：*Overall framework for node-risk learning, edge-risk construction, and downstream hazardous-material routing validation.*

## 图 2：数据规模、标签稀缺性与尾部样本

- 文件：`fig02_data_profile.*`
- 数据源：`paper_results/01_data_statistics/audit_summary.csv`。
- 子图 (a)：2020/2021 年节点数与有向边数；2020 年为 4,696/7,048，2021 年为 5,261/8,115。
- 子图 (b)：有标签节点与高风险节点（等级 6–8）；两年分别为 419/40 和 443/51。
- 目的：说明图规模增长明显，但标签率低且高风险样本极少，从数据层面支撑尾部感知建模的必要性。
- 建议位置：数据与问题定义章节。

## 图 3：节点风险模型性能

- 文件：`fig03_node_model_performance.*`
- 数据源：`outputs_10seed/models/*_10seed_summary.csv`，正式 Split B 的 `data_2021_test`。
- 四个指标：MAE（低为优）、高风险 PR-AUC（高为优）、Recall@6–8（高为优）、高风险漏判率（低为优）。
- 图形：横向条形图；误差条为 10 个模型随机种子的标准差；Stable-Tail GNN 用橙色突出。
- 主要信息：Stable-Tail GNN 的 MAE 为 1.209，在图模型中最低；PR-AUC 为 0.372，为所列模型最高。Weighted-GCN 的高风险召回更高，但 MAE 明显更大，体现精度与尾部召回之间的权衡。
- 建议位置：模型对比实验章节。不要只报告 Macro-F1；本任务更应强调有序误差与高风险识别。

## 图 4：边风险矩阵的尾部选择性

- 文件：`fig04_edge_risk_tail_distribution.*`
- 数据源：`tables/risk_distribution_summary_10seed.csv`。
- 指标：P95、P99、Tail gap = P99 − P95；点为 10-seed 均值，误差条为标准差。
- 目的：展示风险矩阵是否能压低普通高分位风险，同时保留对极端边的区分能力。Stable-Tail GNN 的 P95 最低（0.0626），Tail gap 最大（0.3511），说明风险更集中在真正的尾部边，而不是整体抬高。
- 建议位置：风险矩阵构建与性质分析章节。

## 图 5：OD 路径安全—效率权衡

- 文件：`fig05_od_path_tradeoff.*`
- 数据源：`tables/fig4_od_path_comparison_data_10seed.csv`，固定 150 个 OD 对，CVaR-risk 方法。
- 横轴：相对最短跳数路径的 Hop increase；纵轴：总风险下降率；均带 10-seed 标准差。
- 判读：左上方更优。Stable-Tail GNN 以约 10.23% 的跳数增加取得约 85.01% 的总风险下降，是所列方法中总风险下降最高的模型。
- 建议位置：OD 路径验证章节；与 CVaR90、MaxRisk、RE 的完整数值表配套使用。

## 图 6：PyVRP 成本—风险前沿

- 文件：`fig06_pyvrp_beta_tradeoff.*`
- 数据源：`tables/fig5_pyvrp_beta_curve_data_10seed.csv`。
- 横轴：相对最短路线基线的成本增幅；纵轴：全局风险下降率；曲线分别为客户集 A、B；点旁标注风险权重 beta。
- 主要信息：beta 从 0 增大到 2 时，风险下降逐步饱和，而成本继续增加。beta=1 是较清晰的折中点：Set A 约增加 17.17% 成本、降低 63.47% 风险；Set B 约增加 19.86% 成本、降低 59.56% 风险。
- 建议位置：CVRP 下游验证章节；正文应称其为经验 Pareto 前沿，不应宣称已证明全局 Pareto 最优。

## 图 7：风险负担集中度控制的收益与代价

- 文件：`fig07_concentration_effect.*`
- 数据源：`tables/fig6_concentration_improvement_data_10seed.csv`，比较 lambda=1 与 lambda=0。
- 子图 (a)：全局风险、CVaR90、最大车辆风险、Edge Gini、Top-10% burden share 的相对改善。
- 子图 (b)：额外成本百分点。Set A、B 分别约增加 7.0 和 8.6 个百分点。
- 主要信息：集中度惩罚同时改善安全性和边负担公平性，但需要额外成本；这是论文中最直接的成本—安全—公平三目标证据。
- 建议位置：公平性后验分析或扩展实验章节。

## 论文使用建议

- 主文优先使用图 1、3、5、6、7；图 2 和图 4 可根据篇幅放入主文或附录。
- 结果图正文统一说明“点/条为 10-seed 均值，误差条为标准差”。
- 双栏论文优先插入 PDF 或 SVG；Word 稿件使用 600 dpi PNG。
- 不把 `y=0` 解释为低风险，它表示无标签。
- 跨模型 CVRP 安全比较应使用 common evaluator；图 6 是同一 Stable-Tail 风险矩阵内的 beta 灵敏度，因此可直接比较。

## 复现命令

```powershell
.\PyVRP-main\.venv\Scripts\python.exe -B .\hazmat_risk_experiments\scripts\create_publication_research_figures.py
```

