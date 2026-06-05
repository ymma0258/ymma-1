# 危险品运输风险评价创新点与实验设计最终计划

## 1. 总体主线

本文主线固定为：

```text
风险评价模型创新
→ 节点风险连续化
→ 边风险矩阵
→ OD 路径验证
→ PyVRP-CVRP 下游验证
→ 风险公平后验分析
```

研究定位：

- 主创新在风险评价模型和边风险矩阵。
- OD 路径和 PyVRP-CVRP 只做下游验证。
- PyVRP 不承担风险公平约束优化，只输出 CVRP 路线。
- 风险公平通过路线输出后的后验指标计算。

数据设定：

```text
2020：4696 节点，7048 边
2021：5261 节点，8115 边
节点特征：715 维
标签 y=0：无标签
标签 y=1–8：有序风险等级
高风险：y>=6
```

## 2. 主创新点

### 创新 1：轨迹暴露门控尾部感知图风险评价模型

模型名称：

```text
TEG-TailGNN
Trajectory-Exposure Gated Tail-aware GNN
轨迹暴露门控尾部感知图风险评价模型
```

核心思想：

- 风险等级 `1–8` 是有序标签，损失函数应体现预测等级距离。
- 高风险 `6–8` 样本稀疏，需要高风险 BCE 辅助任务降低漏判。
- Top-k 尾部样本损失用于强调难样本和尾部风险。
- `edge_attribute` 作为轨迹暴露强度，进入边门控图传播。

模型结构：

```text
输入：
  x_i：节点 715 维特征
  edge_index：区域关联边
  edge_attribute：轨迹暴露边权 w_ij

网络：
  Linear(715 → hidden)
  Edge-gated graph layer
  Edge-gated graph layer
  Dropout
  Classifier(hidden → 8)

输出：
  p_i,1 ... p_i,8
  S_i = sum(k * p_i,k)
  P_high = p_i,6 + p_i,7 + p_i,8
```

边门控：

```text
g_ij = sigmoid(W_e w_ij + W_h [h_i || h_j])
h_i^(l+1) = σ( sum_j g_ij W h_j^(l) )
```

训练分两阶段：

```text
阶段 1：L = L_ce + 0.5 L_ord
阶段 2：L = L_ce + α1 L_ord + α2 L_hr + α3 L_topk
默认：α1=0.5, α2=1.0, α3=0.3 或 0.5
```

### 创新 2：连续边风险与 5×8 风险矩阵展示

节点风险：

```text
S_i = sum(k * p_i,k), k=1,...,8
S_i_norm = (S_i - 1) / 7
```

边暴露归一化：

```text
w_ij_norm = edge_attribute_ij
如有极端值：
w_ij_norm = (min(w_ij, P99) - min(w)) / (P99 - min(w) + ε)
```

主边风险：

```text
R_ij = w_ij_norm * max(S_i_norm, S_j_norm)
```

路径和 VRP 使用连续 `R_ij`；5×8 风险矩阵只用于解释展示：

```text
P_level：w_ij 按分位数划分为 1–5
C_level：max(S_i, S_j) 映射为 1–8
RiskLevel = P_level × C_level
```

### 创新 3：成本—尾部风险—公平性的下游验证

验证分两层：

- 区域 OD 路径验证。
- PyVRP-CVRP 下游验证。

风险公平分三层：

| 层面 | 指标 |
|---|---|
| 路径层 | RE、HHI、Gini |
| 车辆层 | Vehicle Risk Gini、Risk Variance、Max Vehicle Risk |
| 边负担层 | Edge Burden Gini-used、Top10% Burden Share、Max Edge Burden |

## 3. 实验阶段

### 阶段 1：数据审计

统计节点数、边数、标签分布、有标签节点数、高风险样本数、`edge_attribute`
分布、图连通性、最大连通分量、最大强连通分量、特征标准化情况。

主实验将区域图无向化，若同时存在 `i→j` 和 `j→i`：

```text
w_ij_undirected = max(w_ij, w_ji)
```

### 阶段 2：风险评价模型训练与对比

数据划分：

- 实验 A：2020 有标签 80% 训练、20% 验证；2021 全部有标签测试。
- 实验 B：2020 全部有标签 + 2021 有标签 50% 训练；2021 剩余 50% 测试。
- 实验 C：2021 有标签 50% 训练、50% 测试，作为同年对照。

对比组：

| 对比组 | 目的 |
|---|---|
| MLP + CE | 节点特征预测能力 |
| GCN + CE | 基础图模型 |
| Weighted-GCN + CE | edge_attribute 是否有效 |
| Edge-GAT + CE | 边权注意力是否有效 |
| TEG-GNN + CE | 边门控结构是否有效 |
| TEG-GNN + CE + Ordinal | 有序损失贡献 |
| TEG-TailGNN + Full Loss | 最终模型 |

指标：Macro-F1、Weighted-F1、MAE、QWK、Recall@6-8、Precision@6-8、
PR-AUC、High-risk false negative rate。

### 阶段 3：核心消融与扩展消融

核心消融：

```text
Full TEG-TailGNN
w/o edge_attribute
w/o edge gate
w/o ordinal loss
w/o high-risk BCE
w/o Top-k loss
```

扩展消融：

```text
伪标签
跨年对齐
不确定性估计
Tail amplification 边风险公式
Uncertainty-aware 边风险公式
```

### 阶段 4：节点风险输出与边风险矩阵

保存每个节点：

```text
p_i,k
S_i
S_i_norm
P_high
```

构建连续边风险和 5×8 风险矩阵展示。辅助上界使用 Label-risk Oracle：
有标签节点 `S_i = y_i`，无标签节点使用模型预测值或邻居均值。

### 阶段 5：区域 OD 路径验证

主实验使用无向化区域图和最大连通分量。OD 类型：

```text
高风险 → 高风险
高风险 → 普通风险
普通风险 → 高风险
```

每组 30–50 对，总计 100–150 对。高风险节点优先使用模型预测风险
Top 20%，真实标签只用于结果评价，不用于测试年 OD/customer 选择。

方法：Hop-shortest、Mean-risk、CVaR-risk、CVaR + Concentration。

主报告：Hop、Mean Risk、MaxRisk、CVaR80、CVaR90、RE、HHI、Gini、
Hop Increase、Risk Reduction。

### 阶段 6：PyVRP-CVRP 下游验证

构造 Risk-CVRP-20/50/100，主实验用 50 客户。

Depot：最大连通分量中暴露强度最高节点。

客户集 A，主实验：

```text
50%：模型预测风险 Top 20%
30%：轨迹暴露 Top 20%
20%：普通节点
```

客户集 B，补充实验：

```text
30%：模型预测风险 Top 20%
30%：轨迹暴露 Top 20%
40%：普通节点
```

主实验 demand 为 1，容量：

```text
n=20,  m=4,  capacity=5
n=50,  m=5,  capacity=10
n=100, m=10, capacity=10
```

主实验固定底层路径：

```text
D_ab = Hop(P_ab^hop)
Q_ab = sum(R_ij), for (i,j) in P_ab^hop
D_ab_norm = (D_ab - min(D)) / (max(D) - min(D) + ε)
Q_ab_norm = (Q_ab - min(Q)) / (max(Q) - min(Q) + ε)
C_ab = D_ab_norm + β Q_ab_norm
β = 0, 0.25, 0.5, 1.0, 2.0
```

PyVRP 输入前整数化：

```text
C_ab_int = round(scale * C_ab)
scale = 1000 或 10000
```

求解设置：seeds `0,1,2,3,4`，每次 `max_runtime=10s`。

后验指标：Total Cost、Cost Increase、Global Risk、Risk Reduction、
Global CVaR90、Max Vehicle Risk、Vehicle Gini、Edge Burden Gini-used、
Top10% Burden Share。

## 4. 最终执行顺序

```text
Step 1：数据审计
Step 2：训练并比较 MLP / GCN / Weighted-GCN / Edge-GAT / TEG-GNN / TEG-TailGNN
Step 3：完成 A 纯跨年、B 跨年适配、C 同年对照
Step 4：核心消融
Step 5：输出节点风险 p_i,k / S_i / S_i_norm / P_high
Step 6：构建连续 R_ij 和 5×8 风险矩阵
Step 7：区域 OD 路径验证
Step 8：构造 Risk-CVRP-20/50/100
Step 9：PyVRP-CVRP 下游求解
Step 10：车辆层、路径层、边负担层风险公平后验分析
Step 11：统计显著性检验和结果表汇总
```

## 5. 明确不做

```text
不把 y=0 当作低风险。
不使用 5×5 风险矩阵。
不把 PyVRP 写成风险公平优化器。
不把 Risk-only 放主实验。
不使用测试真实标签进行 OD/customer 选择。
不把 hop count 解释为真实道路距离。
不把 Path Alignment 放主表。
不跑 PyVRP 官方正式基准。
```

