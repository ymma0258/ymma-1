# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.190006 | 0.000% | 0.239074 | 2.708218 | 0.216232 | 0.867744 | 88.988% |
| 0.5 | 0 | 168009.1 | 14.502% | 5.390378 | 34.183% | 0.145931 | 1.914142 | 0.259723 | 0.848857 | 85.360% |
| 1 | 0 | 181518.2 | 23.708% | 3.745628 | 54.266% | 0.083203 | 1.531171 | 0.343902 | 0.817083 | 80.293% |
| 1.5 | 0 | 191255.7 | 30.345% | 3.137343 | 61.693% | 0.064835 | 1.240117 | 0.303888 | 0.799141 | 77.124% |
| 2 | 0 | 200726.5 | 36.799% | 3.061956 | 62.614% | 0.062957 | 1.242115 | 0.321020 | 0.793943 | 76.430% |
| 3 | 0 | 219018.2 | 49.265% | 2.854744 | 65.144% | 0.058581 | 1.233085 | 0.354645 | 0.776456 | 73.961% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
