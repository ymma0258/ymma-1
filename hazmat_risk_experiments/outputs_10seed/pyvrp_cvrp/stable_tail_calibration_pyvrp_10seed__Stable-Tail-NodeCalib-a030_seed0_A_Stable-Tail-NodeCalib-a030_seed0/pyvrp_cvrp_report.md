# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.852104 | 0.000% | 0.233017 | 2.451519 | 0.211893 | 0.884211 | 90.399% |
| 0.25 | 0 | 142529.6 | 6.367% | 4.971085 | 36.691% | 0.149949 | 1.685790 | 0.242892 | 0.866725 | 87.194% |
| 0.5 | 0 | 148114.8 | 10.535% | 3.573956 | 54.484% | 0.105021 | 1.388297 | 0.301993 | 0.831333 | 82.271% |
| 1 | 0 | 156029.4 | 16.442% | 2.370317 | 69.813% | 0.050443 | 0.998954 | 0.325375 | 0.776801 | 74.158% |
| 2 | 0 | 168094.2 | 25.445% | 1.765778 | 77.512% | 0.033862 | 0.571217 | 0.238509 | 0.729047 | 66.523% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
