# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 7.502219 | 0.000% | 0.245241 | 2.639920 | 0.231705 | 0.869345 | 88.889% |
| 0.25 | 0 | 142333.4 | 5.957% | 4.482474 | 40.251% | 0.129356 | 1.413711 | 0.209385 | 0.844639 | 85.592% |
| 0.5 | 0 | 148523.7 | 10.565% | 4.142074 | 44.789% | 0.121470 | 1.466641 | 0.225852 | 0.837015 | 84.449% |
| 1 | 0 | 157592.2 | 17.316% | 2.700792 | 64.000% | 0.072773 | 0.923614 | 0.256143 | 0.788921 | 77.058% |
| 2 | 0 | 171900.0 | 27.967% | 2.335940 | 68.863% | 0.053380 | 0.815436 | 0.254569 | 0.766635 | 73.469% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
