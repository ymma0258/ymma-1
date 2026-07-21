# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 9.394894 | 0.000% | 0.298096 | 2.606251 | 0.159472 | 0.874051 | 89.801% |
| 0.25 | 0 | 142102.7 | 5.943% | 6.130817 | 34.743% | 0.186558 | 1.881125 | 0.195444 | 0.861035 | 87.219% |
| 0.5 | 0 | 147947.7 | 10.300% | 4.890306 | 47.947% | 0.140501 | 1.681482 | 0.222221 | 0.842796 | 84.379% |
| 1 | 0 | 156620.6 | 16.766% | 3.389460 | 63.922% | 0.081373 | 1.057379 | 0.194271 | 0.796113 | 77.522% |
| 2 | 0 | 169615.4 | 26.455% | 2.806724 | 70.125% | 0.057368 | 0.882040 | 0.226747 | 0.777559 | 74.166% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
