# Stable-Tail calibration Raw P_high 最终检查报告

日期：2026-07-16

## 1. 结论

四类 Stable-Tail 后处理校准现已按目标公式默认使用原始 `P_high`，不再默认把 `P_high < 0.5` 清零。旧的阈值行为仍作为显式的 `gate`/`Gate05` 对照保留，Raw 与 Gate05 的目录、标签、manifest、流水线阶段和汇总文件彼此分离。

本次正式 Raw 实验完整跑通风险矩阵、固定 OD、PyVRP、共同风险矩阵路线评价、负载感知路线评价和预算汇总，全部失败清单为空。

当前 A/B 探索性评价中，综合最优 Raw 候选为 `Stable-Tail-TailOnlyRaw-a030`。它在六项核心下游指标中取得五项最优；`Stable-Tail-EdgeTailRaw-a030` 在 `MaxVehicle-CVaR90 AUBRC` 上最优。该结论仍属于同一评价集上的候选筛选结果，不能表述为经过独立外部验证的最终最优模型。

## 2. 代码修复

- `export_stable_tail_calibrated_risk_matrix.py`
  - schema 升级为 v4。
  - 新增 `--p-high-mode raw|gate`，默认 `raw`。
  - 新增 `--p-high-gate-threshold`，默认 `0.5`，仅在 `gate` 模式生效。
  - EdgeTail、TailOnly、NodeCalib、MatrixEns 四个公式统一使用 `P_high_used`。
  - meta 明确记录 mode、threshold、raw/used 统计、公式、基础风险目录和创建时间。
- `run_stable_tail_calibration_exports.py`
  - Raw/Gate05 使用不同标签、目录和 manifest。
- `run_10seed_pipeline.py`
  - 新增 Raw/Gate05 独立的 risk、OD、PyVRP、budget-sweep 阶段。
  - dry-run 不再写 run-list。
  - PyVRP 阶段在启动前检查当前 Python 环境是否安装 `pyvrp`。
- `summarize_stable_tail_calibration.py`
  - 分别输出 Raw、Gate05 和逐配置 Raw-vs-Gate05 表。
- `tests/test_stable_tail_calibration.py`
  - 同时覆盖 Raw 原值使用与 Gate05 阈值行为。

## 3. 完整性检查

| 阶段 | 结果 |
|---|---:|
| Raw 风险源 manifest | 170 = 17 配置 × 10 模型种子 |
| Raw meta 检查 | 170/170 为 schema v4、mode=raw |
| Raw/used P_high 统计 | 170/170 的 min/max/mean 完全一致 |
| 固定 OD 汇总 | 340 行，0 失败 |
| PyVRP 汇总 | 1700 行，0 失败 |
| 共同路线汇总 | 1700 行；detail 17000 行，0 失败 |
| 负载路线汇总 | 1700 行；detail 17000 行，0 失败 |
| 预算明细/配置汇总/A-B 平均 | 2380 / 34 / 17 行 |
| Python 脚本编译 | 55/55 通过 |
| 校准单元测试 | 7/7 通过 |

pytest 仅因工作区权限无法创建 `.pytest_cache` 给出缓存警告，不影响测试结果。

## 4. 节点风险评价

四类校准是风险矩阵后处理，不重新训练节点分类器，因此不能把下游风险改善解释为节点分类精度提升。原始 10-seed 节点测试中：

- `SGFormer-adapted` 的 Macro-F1、QWK、高风险召回最好：0.321669、0.371682、0.369231；高风险漏报率最低：0.630769。
- `GCN` 的 Weighted-F1 最好：0.621238。
- `GraphSAGE` 的高风险 Precision 和 PR-AUC 最好：0.486390、0.376279。
- `GraphSAGE-TEG-Gate` 的 Brier/ECE 最好：0.494035、0.085356。
- `Stable-Tail GNN`：Macro-F1 0.289627、Weighted-F1 0.619415、MAE 1.266622、QWK 0.290427、高风险 Recall 0.246154、PR-AUC 0.365928、Brier 0.503772、ECE 0.093225。

因此，Stable-Tail GNN 的优势主要体现在经过路线优化后的风险表现，而不是所有节点分类指标均领先。

## 5. OD 路径验证

`Stable-Tail-TailOnlyRaw-a030` 相对 hop-shortest 的 10-seed 平均结果：

| 指标 | 结果 |
|---|---:|
| 跳数增加 | 10.236% ± 0.598% |
| 总风险下降 | 86.136% ± 0.580% |
| CVaR90 下降 | 90.636% ± 0.571% |
| 最大边风险下降 | 91.223% ± 0.569% |
| 风险暴露 RE 下降 | 92.290% ± 0.514% |

原始 `Stable-Tail GNN` 对应为 10.228%、84.774%、90.083%、90.785%、91.953%。Raw TailOnly-a030 在几乎相同跳数代价下进一步降低四类风险。

## 6. 下游路线和预算结果

数值越低越好。

| 模型 | AvgRisk@B | Common AUBRC | CVaR90 | CVaR95 | Load-CVaR90 | MaxVehicle-CVaR90 |
|---|---:|---:|---:|---:|---:|---:|
| TailOnlyRaw-a030 | 3.972190 | 1.162222 | 0.028013 | 0.051012 | 0.016739 | 0.049928 |
| EdgeTailRaw-a030 | 4.008143 | 1.172975 | 0.028266 | 0.051407 | 0.016766 | **0.049511** |
| MatrixEnsRaw-r010 | 4.037462 | 1.179508 | 0.028506 | 0.052022 | 0.016927 | 0.051683 |
| MatrixEnsGate05-r010 | 4.005970 | 1.171320 | 0.028455 | 0.051323 | **0.016649** | 0.050608 |
| Stable-Tail GNN | 4.057116 | 1.189196 | 0.028834 | 0.052469 | 0.017251 | 0.051798 |
| GraphSAGE-TEG-Gate | 4.031325 | 1.185319 | 0.028879 | 0.052173 | 0.016838 | 0.051846 |

TailOnlyRaw-a030 相对 Stable-Tail GNN 的六项下降幅度依次为 2.09%、2.27%、2.85%、2.78%、2.96%、3.61%。

Raw 并非对每个超参数都优于 Gate05：17 个配对中，Raw 在六项指标上的胜出配置数分别为 11、11、10、10、11、10。特别是 `MatrixEnsRaw-r010` 六项均差于 `MatrixEnsGate05-r010`；这说明修复保证的是公式正确性，不保证每个 Raw 配置数值都更优。

## 7. 推荐表述

可以表述：

> 在原始 P_high 公式、固定 10 模型种子、固定 OD、固定 A/B 客户集和当前预算评价下，TailOnlyRaw-a030 是综合表现最好的 Raw 校准候选；EdgeTailRaw-a030 在最大单车尾部风险上最优。

不应表述：

> TailOnlyRaw-a030 已经通过独立验证，是无条件的最终最优模型。

若论文需要确认性“最终模型”，仍应预先固定超参数，并在未参与本次 17 候选筛选的新客户集合或外层验证集上仅评估一次。

## 8. 主要结果文件

- Raw/Gate05 总结：`outputs_10seed/pyvrp_cvrp/stable_tail_calibration_raw_budget_sweep_10seed/`
- Raw-vs-Gate05：`raw_vs_gate05_comparison.csv`
- Raw 最优指标：`best_raw_calibration_by_metric.csv`
- 固定 OD：`outputs_10seed/od_paths/stable_tail_calibration_raw_od_10seed/`
- PyVRP：`outputs_10seed/pyvrp_cvrp/stable_tail_calibration_raw_pyvrp_10seed/`
- 共同路线：`outputs_10seed/pyvrp_cvrp/stable_tail_calibration_raw_common_eval_10seed/`
- 负载路线：`outputs_10seed/pyvrp_cvrp/stable_tail_calibration_raw_load_eval_10seed/`
