# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.392419 | 0.000% | 0.252220 | 2.715405 | 0.232249 | 0.851789 | 88.373% |
| 0.25 | 0 | 157182.2 | 6.977% | 7.365015 | 12.242% | 0.197680 | 2.361882 | 0.215074 | 0.849979 | 88.041% |
| 0.5 | 0 | 165996.5 | 12.976% | 5.640976 | 32.785% | 0.132269 | 1.683944 | 0.184934 | 0.829866 | 84.891% |
| 1 | 0 | 178752.4 | 21.658% | 4.245403 | 49.414% | 0.108028 | 1.394258 | 0.233696 | 0.797948 | 80.407% |
| 2 | 0 | 195922.4 | 33.343% | 2.924076 | 65.158% | 0.058831 | 1.014950 | 0.271847 | 0.745541 | 72.067% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
