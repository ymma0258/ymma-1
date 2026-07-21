# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.075303 | 0.000% | 0.258435 | 2.672908 | 0.225600 | 0.883377 | 90.140% |
| 0.25 | 0 | 142474.4 | 6.062% | 4.614920 | 42.851% | 0.136782 | 1.562963 | 0.230661 | 0.860006 | 86.128% |
| 0.5 | 0 | 148137.9 | 10.278% | 3.812191 | 52.792% | 0.112424 | 1.359873 | 0.264752 | 0.841928 | 83.550% |
| 1 | 0 | 155870.8 | 16.035% | 2.406748 | 70.196% | 0.054506 | 0.970069 | 0.284684 | 0.779871 | 74.340% |
| 2 | 0 | 167857.5 | 24.958% | 1.822416 | 77.432% | 0.033088 | 0.646168 | 0.271555 | 0.729437 | 66.804% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
