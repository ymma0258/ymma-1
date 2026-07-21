# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 7.261436 | 0.000% | 0.222733 | 2.497016 | 0.247356 | 0.872327 | 89.289% |
| 0.25 | 0 | 155590.3 | 5.606% | 5.931720 | 18.312% | 0.145615 | 2.149820 | 0.276014 | 0.867120 | 88.181% |
| 0.5 | 0 | 163724.8 | 11.127% | 4.723686 | 34.948% | 0.119551 | 1.842768 | 0.302187 | 0.854810 | 85.624% |
| 1 | 0 | 175365.8 | 19.029% | 3.505974 | 51.718% | 0.088931 | 1.480415 | 0.324693 | 0.834688 | 82.054% |
| 2 | 0 | 192430.4 | 30.611% | 2.891969 | 60.174% | 0.072216 | 1.297983 | 0.331764 | 0.814285 | 78.443% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
