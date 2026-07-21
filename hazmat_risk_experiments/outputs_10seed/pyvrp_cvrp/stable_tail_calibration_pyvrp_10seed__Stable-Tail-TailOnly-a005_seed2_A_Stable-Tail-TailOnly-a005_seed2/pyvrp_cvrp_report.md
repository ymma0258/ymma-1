# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.980893 | 0.000% | 0.301486 | 2.865986 | 0.200982 | 0.879351 | 90.044% |
| 0.25 | 0 | 142481.2 | 6.172% | 6.196413 | 31.004% | 0.179303 | 2.127792 | 0.254234 | 0.867628 | 88.135% |
| 0.5 | 0 | 148568.7 | 10.708% | 4.837136 | 46.140% | 0.141537 | 1.638439 | 0.249000 | 0.853211 | 85.386% |
| 1 | 0 | 157768.9 | 17.564% | 3.247773 | 63.837% | 0.088733 | 1.196754 | 0.318520 | 0.809302 | 78.802% |
| 2 | 0 | 171828.0 | 28.040% | 2.896889 | 67.744% | 0.070156 | 1.174096 | 0.328784 | 0.795851 | 76.397% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
