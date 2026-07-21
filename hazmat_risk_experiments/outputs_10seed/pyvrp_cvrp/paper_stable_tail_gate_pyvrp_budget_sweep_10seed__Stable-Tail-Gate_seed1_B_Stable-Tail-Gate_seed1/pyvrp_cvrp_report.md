# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.499939 | 0.000% | 0.247560 | 2.782159 | 0.230104 | 0.858075 | 88.606% |
| 0.25 | 0 | 156648.0 | 6.614% | 7.354934 | 13.471% | 0.207950 | 2.328155 | 0.211209 | 0.854036 | 87.877% |
| 0.5 | 0 | 164935.4 | 12.254% | 5.836171 | 31.339% | 0.156706 | 1.724845 | 0.185384 | 0.837865 | 85.075% |
| 1 | 0 | 175431.5 | 19.398% | 3.564715 | 58.062% | 0.074499 | 1.237262 | 0.261095 | 0.783211 | 76.949% |
| 2 | 0 | 190838.3 | 29.883% | 2.963057 | 65.140% | 0.061476 | 0.880355 | 0.237132 | 0.757970 | 72.962% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
