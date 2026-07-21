# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.139498 | 0.000% | 0.255324 | 2.445728 | 0.169474 | 0.864101 | 88.136% |
| 0.25 | 0 | 143587.1 | 6.890% | 4.850812 | 40.404% | 0.139102 | 1.653316 | 0.271704 | 0.840173 | 84.557% |
| 0.5 | 0 | 149704.5 | 11.444% | 4.096171 | 49.675% | 0.119256 | 1.536638 | 0.301784 | 0.819852 | 81.989% |
| 1 | 0 | 159167.2 | 18.488% | 2.922614 | 64.093% | 0.078142 | 0.942413 | 0.246825 | 0.776885 | 75.688% |
| 2 | 0 | 173580.5 | 29.218% | 2.252095 | 72.331% | 0.051757 | 0.841128 | 0.291218 | 0.726561 | 68.727% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
