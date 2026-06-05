# Final Figures and Result Files

本目录汇总 Stable-Tail GNN 最终实验的 6 张论文图和配套结果表。

## 图 1：整体实验框架图
- 文件：`figures/fig1_overall_experiment_framework.png`
- 内容：车辆轨迹图数据 -> Stable-Tail GNN -> 节点风险 -> floor_0.01 边风险矩阵 -> OD 路径验证 -> PyVRP-CVRP 下游验证 -> 风险/成本/公平性评价。

## 图 2：模型结构图
- 文件：`figures/fig2_stable_tail_gnn_structure.png`
- 内容：GCN 稳定分支与 TEG 轨迹暴露门控分支 concat 融合，输出 1-8 风险概率、S_i 和 P_high。

## 图 3：风险矩阵分布图
- 文件：`figures/fig3_risk_matrix_distribution.png`
- 表格：`tables/fig3_risk_distribution_data.csv`、`tables/fig3_floor_diagnostics_data.csv`
- 结论：TEG-low 的 P99 和 Std 更高，说明尾部敏感；raw 矩阵零风险边比例约 93.15%，floor_0.01 将零风险比例降为 0。

## 图 4：OD 路径对比图
- 文件：`figures/fig4_od_path_comparison.png`
- 表格：`tables/fig4_od_path_comparison_data.csv`
- 结论：CVaR-risk 在少量 Hop 增加下显著降低 Total Risk、CVaR90 和 RE；CVaR+Concentration 进一步降低 RE，但 Hop 代价更高。

## 图 5：PyVRP beta 成本-风险折中曲线
- 文件：`figures/fig5_pyvrp_beta_tradeoff.png`
- 表格：`tables/fig5_pyvrp_beta_curve_data.csv`
- 结论：beta 增大时 Risk Reduction 上升、CVaR90 下降，Edge Burden Gini 总体下降，体现成本-风险折中。

## 图 6：concentration-aware lambda 改善图
- 文件：`figures/fig6_concentration_aware_improvement.png`
- 表格：`tables/fig6_concentration_improvement_data.csv`
- 结论：lambda=1 相比 lambda=0 能降低 Global Risk、CVaR90、Edge Burden Gini 和 Top10% Burden Share，支持边负担公平扩展。


## Additional Risk Distribution Figures

### 图 7：风险分位数折线图
- 文件：`figures/fig7_risk_quantile_curves.png`
- 表格：`tables/fig7_quantile_curve_data.csv`
- 用途：展示 P50/P75/P90/P95/P99/Max 的分位数曲线，突出 Stable-Tail GNN 低中分位较低但 P99 保持较高。

### 图 8：P95-P99-Max 尾部放大柱状图
- 文件：`figures/fig8_tail_risk_zoom.png`
- 表格：`tables/fig8_tail_zoom_data.csv`
- 用途：只比较 P95、P99 和 Max，突出最终模型的尾部选择性。

### 图 9：raw/floor 退化修复图
- 文件：`figures/fig9_raw_floor_repair.png`
- 表格：`tables/fig9_floor_repair_data.csv`
- 用途：展示 raw 的零风险边退化，以及 floor_0.01 对零风险退化的修复。

### 图 10：风险分布热力图
- 文件：`figures/fig10_risk_distribution_heatmap.png`
- 表格：`tables/fig10_heatmap_normalized_data.csv`
- 用途：按列标准化展示各模型在 Mean/P50/P75/P90/P95/P99/Std/TailGap 上的相对高低。

### 图 11：关键风险指标点图
- 文件：`figures/fig11_risk_metric_dot_plot.png`
- 表格：`tables/fig11_dot_plot_data.csv`
- 用途：用更清爽的点图比较 Mean、P95、P99 和 TailGap。


## Additional Risk Distribution Figures

### 图 7：风险分位数折线图
- 文件：`figures/fig7_risk_quantile_curves.png`
- 表格：`tables/fig7_quantile_curve_data.csv`
- 用途：展示 P50/P75/P90/P95/P99/Max 的分位数曲线，突出 Stable-Tail GNN 低中分位较低但 P99 保持较高。

### 图 8：P95-P99-Max 尾部放大柱状图
- 文件：`figures/fig8_tail_risk_zoom.png`
- 表格：`tables/fig8_tail_zoom_data.csv`
- 用途：只比较 P95、P99 和 Max，突出最终模型的尾部选择性。

### 图 9：raw/floor 退化修复图
- 文件：`figures/fig9_raw_floor_repair.png`
- 表格：`tables/fig9_floor_repair_data.csv`
- 用途：展示 raw 的零风险边退化，以及 floor_0.01 对零风险退化的修复。

### 图 10：风险分布热力图
- 文件：`figures/fig10_risk_distribution_heatmap.png`
- 表格：`tables/fig10_heatmap_normalized_data.csv`
- 用途：按列标准化展示各模型在 Mean/P50/P75/P90/P95/P99/Std/TailGap 上的相对高低。

### 图 11：关键风险指标点图
- 文件：`figures/fig11_risk_metric_dot_plot.png`
- 表格：`tables/fig11_dot_plot_data.csv`
- 用途：用更清爽的点图比较 Mean、P95、P99 和 TailGap。


## Additional Risk Distribution Figures

### 图 7：风险分位数折线图
- 文件：`figures/fig7_risk_quantile_curves.png`
- 表格：`tables/fig7_quantile_curve_data.csv`
- 用途：展示 P50/P75/P90/P95/P99/Max 的分位数曲线，突出 Stable-Tail GNN 低中分位较低但 P99 保持较高。

### 图 8：P95-P99-Max 尾部放大柱状图
- 文件：`figures/fig8_tail_risk_zoom.png`
- 表格：`tables/fig8_tail_zoom_data.csv`
- 用途：只比较 P95、P99 和 Max，突出最终模型的尾部选择性。

### 图 9：raw/floor 退化修复图
- 文件：`figures/fig9_raw_floor_repair.png`
- 表格：`tables/fig9_floor_repair_data.csv`
- 用途：展示 raw 的零风险边退化，以及 floor_0.01 对零风险退化的修复。


## Additional Risk Distribution Figures

### 图 7：风险分位数折线图
- 文件：`figures/fig7_risk_quantile_curves.png`
- 表格：`tables/fig7_quantile_curve_data.csv`
- 用途：展示 P50/P75/P90/P95/P99/Max 的分位数曲线，突出 Stable-Tail GNN 低中分位较低但 P99 保持较高。

### 图 8：P95-P99-Max 尾部放大柱状图
- 文件：`figures/fig8_tail_risk_zoom.png`
- 表格：`tables/fig8_tail_zoom_data.csv`
- 用途：只比较 P95、P99 和 Max，突出最终模型的尾部选择性。

### 图 9：raw/floor 退化修复图
- 文件：`figures/fig9_raw_floor_repair.png`
- 表格：`tables/fig9_floor_repair_data.csv`
- 用途：展示 raw 的零风险边退化，以及 floor_0.01 对零风险退化的修复。


## Additional Risk Distribution Figures

### Figure 7: Tail quantile comparison
- Figure: `figures/fig7_risk_quantile_curves.png`
- Table: `tables/fig7_quantile_curve_data.csv`
- Purpose: compares P95, P99, and TailGap only.

### Figure 10: P95-TailGap scatter
- Figure: `figures/fig10_p95_tailgap_scatter.png`
- Table: `tables/fig10_p95_tailgap_scatter_data.csv`
- Purpose: highlights the low-P95/high-TailGap position of Stable-Tail GNN.

### Figure 11: Relative change compared with GCN
- Figure: `figures/fig11_relative_change_vs_gcn.png`
- Table: `tables/fig11_relative_change_vs_gcn_data.csv`
- Purpose: compares TEG-low and Stable-Tail GNN against GCN on Mean, P95, P99, and TailGap.

### Figure 12: Tail selectivity panels
- Figure: `figures/fig12_tail_selectivity_panels.png`
- Table: `tables/fig12_tail_selectivity_panel_data.csv`
- Purpose: combines the P95-TailGap scatter with relative change against GCN.


## Additional Risk Distribution Figures

### Figure 7: Tail quantile comparison
- Figure: `figures/fig7_risk_quantile_curves.png`
- Table: `tables/fig7_quantile_curve_data.csv`
- Purpose: compares P95, P99, and TailGap only.

### Figure 10: P95-TailGap scatter
- Figure: `figures/fig10_p95_tailgap_scatter.png`
- Table: `tables/fig10_p95_tailgap_scatter_data.csv`
- Purpose: highlights the low-P95/high-TailGap position of Stable-Tail GNN.

### Figure 11: Relative change compared with GCN
- Figure: `figures/fig11_relative_change_vs_gcn.png`
- Table: `tables/fig11_relative_change_vs_gcn_data.csv`
- Purpose: compares TEG-low and Stable-Tail GNN against GCN on Mean, P95, P99, and TailGap.

### Figure 12: Tail selectivity panels
- Figure: `figures/fig12_tail_selectivity_panels.png`
- Table: `tables/fig12_tail_selectivity_panel_data.csv`
- Purpose: combines the P95-TailGap scatter with relative change against GCN.
