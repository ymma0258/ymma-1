# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.958798 | 0.000% | 0.222230 | 2.473239 | 0.188442 | 0.848255 | 87.480% |
| 0.5 | 0 | 148077.0 | 10.507% | 4.080312 | 48.732% | 0.096847 | 1.873240 | 0.366966 | 0.775850 | 78.054% |
| 1 | 0 | 156724.6 | 16.961% | 3.065513 | 61.483% | 0.072187 | 0.853545 | 0.178347 | 0.716529 | 70.861% |
| 1.5 | 0 | 163805.2 | 22.245% | 2.730699 | 65.690% | 0.053803 | 0.870841 | 0.226839 | 0.688420 | 67.260% |
| 2 | 0 | 169794.8 | 26.715% | 2.226260 | 72.028% | 0.037451 | 0.669322 | 0.186368 | 0.622201 | 58.895% |
| 3 | 0 | 180397.2 | 34.627% | 2.273866 | 71.430% | 0.038332 | 0.597880 | 0.150310 | 0.631540 | 60.033% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
