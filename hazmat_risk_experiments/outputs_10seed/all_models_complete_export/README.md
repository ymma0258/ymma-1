# 全模型结果导出索引

- `all_models_all_results_20260721.xlsx`：完整可筛选工作簿。
- `all_models_model_level_summary_20260721.csv`：47 个可比较模型的模型级汇总。

| 表 | 行数 |
|---|---:|
| Model_Master | 47 |
| Node_Test_13 | 13 |
| OD_All | 94 |
| Budget_by_set | 94 |
| Budget_AB_47 | 47 |
| Raw_vs_Gate05 | 17 |
| Raw_manifest_170 | 170 |
| Gate05_manifest_170 | 170 |
| Raw_PyVRP_1700 | 1700 |
| Gate05_PyVRP_1700 | 1700 |
| Raw_Common_1700 | 1700 |
| Gate05_Common_1700 | 1700 |
| Raw_Load_1700 | 1700 |
| Gate05_Load_1700 | 1700 |
| Raw_Budget_Detail | 2380 |
| Gate05_Budget_Detail | 2380 |

Raw 使用未阈值化 P_high；Gate05 为历史 P_high >= 0.5 对照。
校准方案为风险矩阵后处理，故节点分类列对校准行留空。
