# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134265.1 | 0.000% | 7.832340 | 0.000% | 0.239633 | 2.615859 | 0.213861 | 0.882329 | 90.187% |
| 0.25 | 0 | 142503.4 | 6.136% | 4.640834 | 40.748% | 0.140697 | 1.651959 | 0.260151 | 0.861679 | 86.457% |
| 0.5 | 0 | 148389.0 | 10.519% | 3.904297 | 50.152% | 0.116971 | 1.601951 | 0.307806 | 0.845757 | 84.296% |
| 1 | 0 | 156313.6 | 16.422% | 2.413668 | 69.183% | 0.055037 | 0.955847 | 0.284059 | 0.781893 | 74.816% |
| 2 | 0 | 168419.7 | 25.438% | 1.801146 | 77.004% | 0.034005 | 0.568856 | 0.222321 | 0.729713 | 66.470% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
