# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 5.979987 | 0.000% | 0.189336 | 2.109229 | 0.264157 | 0.874213 | 90.025% |
| 0.25 | 0 | 155692.6 | 6.011% | 4.712898 | 21.189% | 0.124272 | 1.513630 | 0.241004 | 0.869691 | 88.562% |
| 0.5 | 0 | 163333.9 | 11.214% | 4.136263 | 30.832% | 0.105368 | 1.357042 | 0.246512 | 0.861060 | 87.063% |
| 1 | 0 | 173177.7 | 17.917% | 2.301832 | 61.508% | 0.054680 | 0.818449 | 0.265257 | 0.812711 | 78.684% |
| 2 | 0 | 187031.2 | 27.350% | 1.947048 | 67.441% | 0.038145 | 0.718772 | 0.278873 | 0.794427 | 75.597% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
