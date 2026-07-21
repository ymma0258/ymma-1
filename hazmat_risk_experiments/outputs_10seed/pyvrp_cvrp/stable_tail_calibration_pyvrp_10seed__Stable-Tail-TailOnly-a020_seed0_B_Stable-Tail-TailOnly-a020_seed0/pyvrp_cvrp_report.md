# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.819158 | 0.000% | 0.214691 | 2.698250 | 0.261361 | 0.881347 | 89.841% |
| 0.25 | 0 | 156217.8 | 6.369% | 6.196849 | 20.748% | 0.149519 | 2.536043 | 0.305621 | 0.869685 | 87.977% |
| 0.5 | 0 | 164457.8 | 11.980% | 4.632059 | 40.760% | 0.115647 | 1.580665 | 0.230795 | 0.850026 | 84.616% |
| 1 | 0 | 174332.2 | 18.703% | 3.086364 | 60.528% | 0.077428 | 1.052512 | 0.241851 | 0.808050 | 77.907% |
| 2 | 0 | 188794.7 | 28.551% | 2.416270 | 69.098% | 0.048516 | 0.853197 | 0.262478 | 0.776805 | 72.272% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
