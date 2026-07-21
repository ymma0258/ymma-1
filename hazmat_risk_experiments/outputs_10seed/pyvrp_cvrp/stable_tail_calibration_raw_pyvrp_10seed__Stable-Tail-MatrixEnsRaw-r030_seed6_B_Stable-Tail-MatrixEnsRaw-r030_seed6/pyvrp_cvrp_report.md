# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 6.340406 | 0.000% | 0.193416 | 2.134367 | 0.233247 | 0.870437 | 89.406% |
| 0.25 | 0 | 157855.0 | 7.192% | 5.583756 | 11.934% | 0.146354 | 1.975323 | 0.271720 | 0.868987 | 89.311% |
| 0.5 | 0 | 168164.5 | 14.193% | 4.359574 | 31.241% | 0.111245 | 1.632681 | 0.295335 | 0.858634 | 86.759% |
| 1 | 0 | 181360.6 | 23.154% | 3.137407 | 50.517% | 0.078231 | 1.276638 | 0.321229 | 0.830388 | 82.053% |
| 2 | 0 | 202399.1 | 37.440% | 2.689693 | 57.579% | 0.069296 | 1.066774 | 0.359942 | 0.823208 | 80.071% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
