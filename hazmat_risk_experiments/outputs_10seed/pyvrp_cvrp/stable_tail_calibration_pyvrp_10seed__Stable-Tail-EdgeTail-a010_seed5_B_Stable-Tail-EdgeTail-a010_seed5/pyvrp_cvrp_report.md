# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 7.660464 | 0.000% | 0.225893 | 2.629005 | 0.242661 | 0.873242 | 88.883% |
| 0.25 | 0 | 156674.1 | 6.390% | 6.661055 | 13.046% | 0.182364 | 2.243935 | 0.237614 | 0.869605 | 88.315% |
| 0.5 | 0 | 165614.9 | 12.461% | 4.991743 | 34.838% | 0.115417 | 1.668467 | 0.245702 | 0.844900 | 84.449% |
| 1 | 0 | 176288.8 | 19.709% | 3.279619 | 57.188% | 0.079775 | 1.211802 | 0.310752 | 0.811099 | 78.399% |
| 2 | 0 | 191777.5 | 30.227% | 2.792788 | 63.543% | 0.067492 | 0.909110 | 0.270716 | 0.794288 | 75.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
