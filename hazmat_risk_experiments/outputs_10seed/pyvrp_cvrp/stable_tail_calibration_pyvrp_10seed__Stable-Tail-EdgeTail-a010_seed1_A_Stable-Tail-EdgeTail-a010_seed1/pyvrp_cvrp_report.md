# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 9.446822 | 0.000% | 0.310835 | 2.658858 | 0.164599 | 0.871355 | 89.644% |
| 0.25 | 0 | 142353.6 | 5.867% | 6.292412 | 33.391% | 0.185799 | 1.996015 | 0.216174 | 0.863565 | 87.462% |
| 0.5 | 0 | 148017.1 | 10.079% | 4.795221 | 49.240% | 0.128589 | 1.763171 | 0.264518 | 0.844203 | 84.335% |
| 1 | 0 | 156530.3 | 16.410% | 3.227460 | 65.835% | 0.078128 | 1.096763 | 0.239693 | 0.792894 | 77.002% |
| 2 | 0 | 169409.1 | 25.988% | 2.679449 | 71.637% | 0.053225 | 0.838857 | 0.230111 | 0.766947 | 72.737% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
