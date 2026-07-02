# Cost-Constrained Route Risk

Routes are re-evaluated on one common matrix. Risk@B is the minimum risk among routes with CostInc <= B. PyVRP itself is not modified.

| Method | Set | Common Risk @20% | CVaR90 @25% | Load Risk @30% | Edge Gini @25% | Top10 Share @25% |
|---|---|---:|---:|---:|---:|---:|
| A_GCN_seed0 | A | nan | 0.059832 | 1.310514 | 0.729469 | 72.212% |
| A_GCN_seed1 | A | nan | 0.061855 | 1.230926 | 0.733846 | 72.878% |
| A_GCN_seed2 | A | nan | 0.086448 | 1.395110 | 0.753277 | 75.289% |
| A_GCN_seed3 | A | nan | 0.066287 | 1.356738 | 0.734403 | 72.800% |
| A_GCN_seed4 | A | nan | 0.078381 | 1.365381 | 0.741956 | 73.943% |
| A_GCN_seed5 | A | nan | 0.071899 | 1.331016 | 0.742430 | 73.845% |
| A_GCN_seed6 | A | nan | 0.057982 | 1.375130 | 0.730222 | 72.248% |
| A_GCN_seed7 | A | nan | 0.074256 | 1.317341 | 0.746574 | 74.341% |
| A_GCN_seed8 | A | nan | 0.083214 | 1.291338 | 0.753066 | 75.402% |
| A_GCN_seed9 | A | nan | 0.069482 | 1.376325 | 0.733059 | 72.724% |
| A_Stable-Tail-GNN_seed0 | A | nan | 0.059852 | 1.182389 | 0.719417 | 70.909% |
| A_Stable-Tail-GNN_seed1 | A | nan | 0.048784 | 1.301533 | 0.725642 | 71.503% |
| A_Stable-Tail-GNN_seed2 | A | nan | 0.075278 | 1.387011 | 0.743547 | 74.033% |
| A_Stable-Tail-GNN_seed3 | A | nan | 0.064050 | 1.364895 | 0.733916 | 72.941% |
| A_Stable-Tail-GNN_seed4 | A | nan | 0.078697 | 1.332222 | 0.749914 | 74.726% |
| A_Stable-Tail-GNN_seed5 | A | nan | 0.053429 | 1.345633 | 0.722912 | 71.396% |
| A_Stable-Tail-GNN_seed6 | A | nan | 0.054551 | 1.305815 | 0.737396 | 72.822% |
| A_Stable-Tail-GNN_seed7 | A | nan | 0.049654 | 1.189746 | 0.728181 | 71.880% |
| A_Stable-Tail-GNN_seed8 | A | nan | 0.054594 | 1.199779 | 0.733002 | 72.541% |
| A_Stable-Tail-GNN_seed9 | A | nan | 0.051082 | 1.297657 | 0.728160 | 71.937% |
| A_TEG-low_seed0 | A | nan | 0.071199 | 1.188532 | 0.751814 | 75.046% |
| A_TEG-low_seed1 | A | nan | 0.064355 | 1.224187 | 0.733018 | 72.728% |
| A_TEG-low_seed2 | A | nan | 0.072419 | 1.411568 | 0.738800 | 73.444% |
| A_TEG-low_seed3 | A | nan | 0.065169 | 1.287227 | 0.731574 | 72.396% |
| A_TEG-low_seed4 | A | nan | 0.075228 | 1.403395 | 0.743095 | 74.065% |
| A_TEG-low_seed5 | A | nan | 0.063577 | 1.339811 | 0.737824 | 73.098% |
| A_TEG-low_seed6 | A | nan | 0.072071 | 1.435727 | 0.742347 | 73.922% |
| A_TEG-low_seed7 | A | nan | 0.078578 | 1.425092 | 0.748428 | 74.628% |
| A_TEG-low_seed8 | A | nan | 0.080087 | 1.444288 | 0.749326 | 74.923% |
| A_TEG-low_seed9 | A | nan | 0.064704 | 1.260460 | 0.749641 | 74.917% |
| B_GCN_seed0 | B | nan | 0.095427 | 1.699782 | 0.779775 | 78.104% |
| B_GCN_seed1 | B | nan | 0.095687 | 1.761628 | 0.782660 | 78.710% |
| B_GCN_seed2 | B | nan | 0.100927 | 2.145226 | 0.789228 | 79.368% |
| B_GCN_seed3 | B | nan | 0.110697 | 1.754487 | 0.796475 | 80.412% |
| B_GCN_seed4 | B | nan | 0.098273 | 1.820582 | 0.784946 | 78.690% |
| B_GCN_seed5 | B | nan | 0.087178 | 1.599131 | 0.770200 | 76.912% |
| B_GCN_seed6 | B | nan | 0.092184 | 1.845751 | 0.777440 | 78.141% |
| B_GCN_seed7 | B | nan | 0.107899 | 2.157290 | 0.788962 | 79.593% |
| B_GCN_seed8 | B | nan | 0.091742 | 1.761723 | 0.772591 | 77.488% |
| B_GCN_seed9 | B | nan | 0.096713 | 1.763835 | 0.778527 | 78.285% |
| B_Stable-Tail-GNN_seed0 | B | nan | 0.084869 | 1.635683 | 0.759675 | 75.665% |
| B_Stable-Tail-GNN_seed1 | B | nan | 0.089903 | 1.757444 | 0.771978 | 77.115% |
| B_Stable-Tail-GNN_seed2 | B | nan | 0.096852 | 1.640179 | 0.783501 | 78.878% |
| B_Stable-Tail-GNN_seed3 | B | nan | 0.089820 | 1.669955 | 0.768400 | 77.085% |
| B_Stable-Tail-GNN_seed4 | B | nan | 0.095357 | 1.711230 | 0.775944 | 78.053% |
| B_Stable-Tail-GNN_seed5 | B | nan | 0.090005 | 1.774660 | 0.773443 | 77.610% |
| B_Stable-Tail-GNN_seed6 | B | nan | 0.090509 | 1.692625 | 0.775903 | 78.124% |
| B_Stable-Tail-GNN_seed7 | B | nan | 0.091084 | 1.628358 | 0.764905 | 76.689% |
| B_Stable-Tail-GNN_seed8 | B | nan | 0.096826 | 1.688973 | 0.777203 | 78.189% |
| B_Stable-Tail-GNN_seed9 | B | nan | 0.078361 | 1.598437 | 0.751086 | 74.489% |
| B_TEG-low_seed0 | B | nan | 0.089318 | 1.565146 | 0.767623 | 76.828% |
| B_TEG-low_seed1 | B | nan | 0.098629 | 1.829427 | 0.784121 | 79.375% |
| B_TEG-low_seed2 | B | nan | 0.105193 | 1.761277 | 0.791274 | 79.719% |
| B_TEG-low_seed3 | B | nan | 0.099784 | 1.644581 | 0.781227 | 78.484% |
| B_TEG-low_seed4 | B | nan | 0.100742 | 1.948236 | 0.786760 | 79.473% |
| B_TEG-low_seed5 | B | nan | 0.095973 | 1.792576 | 0.780854 | 78.854% |
| B_TEG-low_seed6 | B | nan | 0.095754 | 1.770384 | 0.782383 | 78.808% |
| B_TEG-low_seed7 | B | nan | 0.087003 | 1.632734 | 0.763047 | 76.279% |
| B_TEG-low_seed8 | B | nan | 0.101088 | 1.778395 | 0.784706 | 79.195% |
| B_TEG-low_seed9 | B | nan | 0.092466 | 1.636580 | 0.771062 | 77.645% |
