# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 4.835952 | 0.000% | 0.144209 | 1.648891 | 0.247275 | 0.870011 | 88.920% |
| 0.25 | 0 | 155311.6 | 5.608% | 4.096123 | 15.299% | 0.102069 | 1.429912 | 0.258542 | 0.865636 | 88.146% |
| 0.5 | 0 | 162971.0 | 10.816% | 3.376519 | 30.179% | 0.085620 | 1.430847 | 0.308329 | 0.855206 | 86.015% |
| 1 | 0 | 174488.8 | 18.648% | 2.569347 | 46.870% | 0.065440 | 1.003996 | 0.293696 | 0.835975 | 82.399% |
| 2 | 0 | 192036.9 | 30.580% | 1.942169 | 59.839% | 0.048016 | 0.836440 | 0.323943 | 0.810176 | 77.729% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
