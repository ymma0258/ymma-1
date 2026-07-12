# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 7.823348 | 0.000% | 0.232458 | 2.263656 | 0.162839 | 0.864492 | 88.299% |
| 0.25 | 0 | 156783.3 | 6.609% | 6.765540 | 13.521% | 0.173435 | 2.072774 | 0.209255 | 0.860242 | 87.921% |
| 0.5 | 0 | 166487.2 | 13.207% | 5.384271 | 31.177% | 0.141673 | 1.646902 | 0.217318 | 0.849599 | 85.628% |
| 1 | 0 | 178682.1 | 21.499% | 3.389797 | 56.671% | 0.081852 | 1.035839 | 0.210380 | 0.793114 | 77.735% |
| 2 | 0 | 197242.9 | 34.120% | 2.942230 | 62.392% | 0.066808 | 0.956281 | 0.252208 | 0.777735 | 74.784% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
