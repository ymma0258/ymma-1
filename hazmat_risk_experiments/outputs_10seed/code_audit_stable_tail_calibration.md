# Stable-Tail GNN 与融合/校准方案代码审计

审计日期：2026-07-15  
审计范围：`hazmat_risk_experiments` 中 Stable-Tail GNN、Stable-Tail-Gate、w/o Tail Loss、4 类后处理校准、10-seed 风险矩阵、OD、PyVRP、统一风险与载重风险评估及汇总脚本。

## 一、结论

当前主干训练、风险矩阵、固定 OD、固定 A/B 客户集合及下游路线评估链路总体完整，10 个模型种子和 10 个求解器种子的产物也完整。Stable-Tail-Gate 是独立的隐藏层门控模型，没有覆盖 Stable-Tail GNN 的 concat 实现；w/o Tail Loss 正确关闭了高风险 BCE 与 top-k 尾部损失。

但是，4 类校准的实际实现与审计任务中给定的数学定义存在一个实质性差异：代码先将 `P_high < 0.5` 的节点清零，再把 `P_high_active` 代入所有校准公式。任务给出的公式使用原始 `P_high`，没有该硬阈值。现有校准结果因此只能归属于“带 0.5 高风险门控的实现”，不能作为原始公式的结果直接引用。

此外，`Stable-Tail-MatrixEns-r010` 是在同一批 A/B 下游评估结果上从 17 个候选中选出，并继续用这批结果报告性能。它是当前评估集上的最佳校准候选，不是经过独立验证后确认的最终最佳模型。论文若直接把它称为最终最优，会有后选择偏差。

综合判定：

- Stable-Tail 基模型实现：通过。
- Stable-Tail-Gate 隔离性：通过。
- w/o Tail Loss 消融：通过。
- 4 类校准产物与“当前代码”：通过数值复算。
- 4 类校准与“任务指定公式”：不完全通过，受 `P_high >= 0.5` 门控影响。
- OD、A/B 路线与统一下游评估公平性：通过。
- 将 `MatrixEns-r010` 无条件认定为论文最终模型：不通过；需要独立校准选择或明确标注探索性结果。

## 二、核心实现核查

### 2.1 Stable-Tail GNN

- 分类头为 8 类，`NUM_CLASSES = 8`，最终线性层输出 8 logits。
- 连续严重度为 `S = sum_k p_k * k`，归一化严重度为 `(S - 1) / 7`。
- `P_high = p_6 + p_7 + p_8`，数组切片 `probs[:, 5:]` 正确。
- exposure-floor 风险为 `w_floor = 0.01 + 0.99*w_raw`，边风险为 `R_ij = w_floor * max(S_i_norm, S_j_norm)`。
- 对 10 个 Stable-Tail 种子的已保存 NPZ 复算：基础风险公式最大绝对误差约 `2.96e-8`，floor 权重最大误差约 `4.77e-9`，`P_high` 复算误差为 0，符合 float32 保存精度。
- 训练采用整图拓扑和无标签特征的 per-year 归一化，标签训练/验证/测试划分保持独立。这是 transductive 设定，不是标签泄漏，但论文方法部分应明确写出。

对应代码：

- `scripts/train_risk_model.py:55-56, 915, 1156-1157, 1370`
- `scripts/export_risk_matrix.py:210-225, 281-324`

### 2.2 Stable-Tail-Gate

Gate 在 GCN 与 TEG 两个隐藏表示之间逐通道融合：

`h = gate * h_gcn + (1 - gate) * h_teg`

它使用独立模型名、checkpoint 和风险矩阵目录。Stable-Tail GNN 继续走 concat + fusion 分支，两者没有混写或覆盖。因此“门控方案是独立模型、基模型保持不变”这一点成立。

对应代码：`scripts/train_risk_model.py:970-974, 1004-1024`。

### 2.3 w/o Tail Loss

该消融保留 Stable-Tail GNN 架构与 ordinal loss，但流水线将 `alpha_hr=0`、`alpha_topk=0`，正确移除了高风险 BCE 和 top-k 尾部损失。它不是另起一套不可比架构。

对应代码：`scripts/train_risk_model.py:1109-1157` 及 `scripts/run_10seed_pipeline.py` 的该模型参数配置。

## 三、4 类融合/校准实现

4 类方案均直接读取 Stable-Tail 基础节点/边 NPZ，不重新训练，不修改 checkpoint、数据划分、OD 或客户集合。170 个导出项由 `17 配置 × 10 模型种子` 构成：EdgeTail 4 个 alpha、TailOnly 4 个 alpha、NodeCalib 4 个 alpha、MatrixEns 5 个 rho。所有种子 0--9 齐全，未发现 fallback。

### 3.1 实际公共前处理

所有方案先执行：

`P_high_active = P_high if P_high >= 0.5 else 0`

再计算 `max(P_high_active_i, P_high_active_j)`。每个种子 5261 个节点中仅约 68--160 个节点激活；7647 条边中 MatrixEns 的正 tail 边约 69--127 条。这一门控已记录在 meta，也被单元测试固定下来，说明它不是偶发错误，而是当前实现的显式设计。

问题在于，审计任务指定的 4 个公式均使用原始 `P_high`。如果研究定义确实是不设阈值，那么当前代码和全部校准结果都不对应目标公式，必须删除该门控后重导风险矩阵并重跑 OD/PyVRP/汇总。

对应代码：`scripts/export_stable_tail_calibrated_risk_matrix.py:136-143`；测试：`tests/test_stable_tail_calibration.py`。

### 3.2 Edge-Tail Correction

当前实际公式：

`R_final = R_base * (1 + alpha * w_raw * max(P_high_active_i, P_high_active_j))`

`w_raw` 使用正确，没有误用 floor 后权重。除公共的 0.5 门控外，结构与目标公式一致。

### 3.3 Tail-Only Correction

当前实际公式：

`R_final = R_base + alpha * gate_q(R_base) * w_raw * max(P_high_active_i, P_high_active_j)`

默认 `q=0.90`，阈值按每个当前 seed/year 的基础风险分位数计算；默认 gate 是 sharpness=20 的 sigmoid，另支持 hard gate。量化范围和元数据完整。除公共 `P_high` 门控外，公式与参数逻辑成立。

### 3.4 Node Calibration

当前实际公式：

`S_final = clip(S_base + alpha * E_mean * P_high_active, 0, 1)`

`R_final = w_floor * max(S_final_i, S_final_j)`

`E_mean` 是节点相邻边原始暴露 `w_raw` 的均值；没有使用测试标签。除公共 `P_high` 门控外，节点校准逻辑成立。

### 3.5 Risk-Matrix Ensemble

当前实际公式：

`R_tail = w_raw * max(P_high_active_i, P_high_active_j)`

`scale = P95(R_base) / P95(positive R_tail)`

`R_final = (1-rho) * R_base + rho * scale * R_tail`

`r010` 正确表示 `rho=0.10`，10 个种子的 meta 均一致。已保存的 `MatrixEns-r010` 与当前代码逐边复算最大误差约 `2.98e-8`。归一化规则明确，但论文必须写清楚它采用“正 tail 边的 P95”，而不是全边 P95；由于正 tail 边很少，该尺度可能对种子较敏感。

将当前结果与“不做 0.5 门控、直接使用原始 P_high”的目标公式相比，边风险相关性仍很高，但最大逐边差异可达约 `0.00731`，足以改变部分路线排序。因此不能假定去掉门控后下游结论不变。

对应代码：`scripts/export_stable_tail_calibrated_risk_matrix.py:168-190`。

## 四、额外实现问题

### 4.1 默认 clip 未包含在目标公式中（中等）

导出脚本默认把校准风险截断到基础风险矩阵最大值。该行为没有出现在任务指定公式中。对 `MatrixEns-r010` 的 10 个种子检查，当前没有边触发该上界，因此 r010 数值不受影响；其他候选仍应分别确认或在论文中披露。

对应代码：`scripts/export_stable_tail_calibrated_risk_matrix.py:302-305`。

### 4.2 `severity_norm` 字段语义变化（中等）

校准导出把 `severity_norm` 写成 `R_final / w_floor`。对 EdgeTail 和 MatrixEns，它不再是单纯的节点严重度，且理论上可超过 1。现有路线评估读取 `R_ij`，因此当前结果未受影响；但任何把该字段当作基础严重度的外部消费者可能被误导。建议增加 `calibrated_risk_over_floor` 字段，或在 schema/meta 中明确新语义。

对应代码：`scripts/export_stable_tail_calibrated_risk_matrix.py:194-215`。

### 4.3 dry-run 会写 run-list（低）

校准 PyVRP 阶段在 dry-run 时仍调用 `write_run_list`，会覆盖运行列表。此次覆盖内容与现有清单一致，没有改变结果，但 dry-run 不应产生写入副作用。

### 4.4 manifest 中 `epochs` 键重复（低）

流水线 manifest payload 有重复的 `epochs` 字典键；Python 保留后一个值，当前产物不受影响，但应清理以避免未来维护歧义。

### 4.5 固定实例的嵌套来源路径陈旧（低）

canonical A/B meta 中保留了指向旧 `outputs` 目录的嵌套 `fixed_instance_meta`。评估器只读取 canonical 文件内已保存的 depot/customers/车辆参数，并不会递归读取旧路径，所以当前公平性不受影响；建议重建 provenance，使归档自包含。

## 五、公平性、完整性与可复现性

- 校准 manifest：170/170 项完整，17 配置 × 10 模型种子。
- 原始 PyVRP：170 个 master chunk，每个 10 条 solver-seed 汇总，未发现失败。
- common-risk 汇总：1700 行，模型种子 0--9、solver seed 0--9、beta `0, 0.25, 0.5, 1, 2` 完整，未发现失败。
- load-aware 汇总：同样完整，未发现失败。
- OD：固定 150 对；校准 OD 汇总 340 行，即 170 source × 2 方法，未发现失败。
- A/B：340 个校准运行的 depot、customer 列表、客户数、车辆数与容量均与 canonical A/B 一致，语义字段零不匹配。
- common-risk 与 load-aware 评估都使用同一 `paper_common_reference_10seed_floor_0p01`。该参考集合包含 5 个主模型 × 10 种子，共 50 个风险目录，权重均为 0.02。
- 各预算点先在相同 `(model seed, set, budget)` 的可行路线中按 common risk 选择一条路线，再在同一条路线计算 AvgRisk、Common AUBRC、CVaR90、CVaR95、Load-CVaR90 和 MaxVehicle-CVaR90；没有为不同指标分别挑路线。
- A/B 最终值是两套等规模客户集的简单平均；每套先汇总 10 solver seeds，再汇总 10 model seeds。

对应代码：

- `scripts/common_evaluate_pyvrp_routes.py:222-275`
- `scripts/common_evaluate_load_aware_routes.py:204-253`
- `scripts/summarize_stable_tail_calibration.py:206-225`

## 六、当前结果与“最好模型”的限定结论

当前汇总中，17 个校准候选的核心平均名次第一是 `Stable-Tail-MatrixEns-r010`。其 A/B 平均结果为：

| 指标 | 当前值 |
|---|---:|
| AvgRisk@预算 10--40% | 4.0059695264 |
| Common AUBRC | 1.1713202400 |
| CVaR90 AUBRC | 0.0284546751 |
| CVaR95 AUBRC | 0.0513230758 |
| Load-CVaR90 AUBRC | 0.0166494875 |
| MaxVehicle-CVaR90 AUBRC | 0.0506084744 |

按 seed 将 A/B 平均后，与基础 Stable-Tail GNN 做配对描述性比较，r010 在六项指标上的平均相对变化约为 `-1.26%`、`-1.50%`、`-1.32%`、`-2.18%`、`-3.48%`、`-2.30%`，对应 10 个 seed 中分别有 9、9、8、9、9、7 个改善。未经候选选择修正的一侧 Wilcoxon p 值分别约为 `0.0049`、`0.0020`、`0.0186`、`0.0049`、`0.0068`、`0.1377`。这些数值只能作为描述性证据：候选已经在同一评估集上被筛选，不能把这些 p 值解释为独立确认性检验。

因此目前可以写：

> 在带 `P_high >= 0.5` 门控、P95-positive 归一化和当前 A/B 探索性评估设置下，`Stable-Tail-MatrixEns-r010` 是表现最好的校准候选。

目前不应写：

> `Stable-Tail-MatrixEns-r010` 已被独立验证为最终最优模型。

## 七、选择偏差与数据泄漏判断

4 类校准公式本身没有读取测试标签，也没有重新训练模型，所以没有发现直接的 test-label leakage。

但 `summarize_stable_tail_calibration.py` 对全部候选在当前 A/B 下游结果上计算核心平均名次，并直接取 `calibration_ab[0]` 作为 best。这是同集调参与报告造成的后选择偏差。对应代码为 `scripts/summarize_stable_tail_calibration.py:278-293, 351-371`。

建议采用以下任一方案：

1. 预先固定一个校准选择集，只用它选择 alpha/rho，再在完全未参与选择的客户集合和 OD 上报告一次最终结果。
2. 做 nested selection：外层客户集合/OD 用于评估，内层集合用于选择校准参数。
3. 若不重跑，则把全部校准结果明确定位为 post-hoc exploratory sensitivity analysis，不作确认性“最终最好”结论。

## 八、验证执行情况

- 55 个脚本执行 `py_compile`：全部通过。
- `python -m unittest hazmat_risk_experiments.tests.test_stable_tail_calibration`：6/6 通过。
- 四阶段校准流水线 dry-run：退出码 0，共生成 191 行命令预览；风险导出、OD、PyVRP、common/load 与预算汇总路径、固定 A/B、固定 OD、beta 和 seed 参数均能贯通。
- 对基础风险和 `MatrixEns-r010` 做了独立数值复算，误差处于 float32 量级。

## 九、建议修复顺序

1. 先确定研究公式是否需要 `P_high >= 0.5`。若不需要，删除公共门控并完整重跑 170 个风险矩阵及全部下游阶段；不要复用现有校准结果。
2. 将参数选择与最终评估分离；至少新增未参与选择的客户集合/OD 验证。
3. 明确并预注册 MatrixEns 的 P95-positive 归一化、clip 行为、q 与 sharpness。
4. 修正 `severity_norm` schema 语义，清理 dry-run 写入、重复 `epochs` 键和 canonical provenance。
5. 在完成 1--3 后，再进行多候选校正后的配对统计检验，决定是否能把 r010 升格为最终模型。

本次审计没有修改训练结构、checkpoint、数据划分、固定 OD、固定客户集合、PyVRP 参数、基础风险公式或既有结果。由于关键问题会改变研究定义并使现有下游结果失效，本次仅形成审计结论，未擅自改公式或重跑实验。
