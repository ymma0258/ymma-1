# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 8.457476 | 0.000% | 0.266029 | 2.707351 | 0.197906 | 0.861090 | 88.379% |
| 0.25 | 0 | 143730.1 | 6.944% | 5.648512 | 33.213% | 0.156223 | 1.826827 | 0.229571 | 0.843364 | 86.614% |
| 0.5 | 0 | 150697.2 | 12.127% | 4.486434 | 46.953% | 0.127476 | 1.574484 | 0.261722 | 0.825248 | 83.586% |
| 1 | 0 | 160123.3 | 19.141% | 3.159955 | 62.637% | 0.072334 | 1.014849 | 0.255186 | 0.774960 | 76.843% |
| 2 | 0 | 175166.9 | 30.334% | 2.330647 | 72.443% | 0.043683 | 0.869316 | 0.297628 | 0.709120 | 68.194% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
