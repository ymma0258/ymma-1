# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 7.962726 | 0.000% | 0.224706 | 2.279949 | 0.161476 | 0.831199 | 85.537% |
| 0.25 | 0 | 158011.8 | 7.396% | 6.914002 | 13.170% | 0.180943 | 2.092124 | 0.183761 | 0.820233 | 83.840% |
| 0.5 | 0 | 167484.7 | 13.834% | 5.694821 | 28.482% | 0.144696 | 1.879075 | 0.228050 | 0.793091 | 80.407% |
| 1 | 0 | 179874.0 | 22.255% | 4.128785 | 48.149% | 0.083967 | 1.541950 | 0.288816 | 0.737583 | 73.483% |
| 2 | 0 | 200185.3 | 36.060% | 3.406277 | 57.222% | 0.062700 | 1.325012 | 0.279650 | 0.694320 | 67.880% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
