# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.335510 | 0.000% | 0.211857 | 2.218565 | 0.178233 | 0.866917 | 88.652% |
| 0.5 | 0 | 148600.4 | 10.898% | 4.159822 | 43.292% | 0.115286 | 1.591034 | 0.289472 | 0.833246 | 83.244% |
| 1 | 0 | 157171.9 | 17.295% | 2.830341 | 61.416% | 0.071418 | 0.892156 | 0.226589 | 0.779814 | 75.946% |
| 1.5 | 0 | 163763.0 | 22.213% | 2.631629 | 64.125% | 0.063395 | 0.871126 | 0.252146 | 0.770782 | 74.250% |
| 2 | 0 | 169944.6 | 26.827% | 2.167867 | 70.447% | 0.043491 | 0.676208 | 0.195083 | 0.728830 | 68.207% |
| 3 | 0 | 179519.9 | 33.972% | 1.837793 | 74.947% | 0.033571 | 0.624388 | 0.246816 | 0.690840 | 62.806% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
