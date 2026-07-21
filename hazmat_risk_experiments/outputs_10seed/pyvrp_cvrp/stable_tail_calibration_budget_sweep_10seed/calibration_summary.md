# Stable-Tail post-processing calibration

All metrics are lower-is-better; AUBRC uses trapezoidal integration over B=10%--40%.

| Rank | Calibration | Avg Risk@B | Common AUBRC | CVaR90 | CVaR95 | LoadCVaR90 | MaxVehCVaR90 | Core score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Stable-Tail-MatrixEns-r010 | 4.0060 | 1.1713 | 0.02845 | 0.05132 | 0.01665 | 0.05061 | 1.750 |
| 2 | Stable-Tail-NodeCalib-a030 | 4.0169 | 1.1730 | 0.02841 | 0.05154 | 0.01682 | 0.05080 | 2.750 |
| 3 | Stable-Tail-TailOnly-a020 | 4.0209 | 1.1766 | 0.02836 | 0.05178 | 0.01696 | 0.05121 | 3.500 |
| 4 | Stable-Tail-NodeCalib-a010 | 4.0148 | 1.1725 | 0.02853 | 0.05184 | 0.01707 | 0.05064 | 5.000 |
| 5 | Stable-Tail-MatrixEns-r040 | 4.0314 | 1.1772 | 0.02848 | 0.05160 | 0.01689 | 0.05075 | 6.250 |
| 6 | Stable-Tail-EdgeTail-a020 | 4.0305 | 1.1771 | 0.02834 | 0.05208 | 0.01708 | 0.05143 | 6.750 |
| 7 | Stable-Tail-MatrixEns-r020 | 4.0238 | 1.1768 | 0.02865 | 0.05189 | 0.01696 | 0.05130 | 8.250 |
| 8 | Stable-Tail-TailOnly-a005 | 4.0389 | 1.1799 | 0.02852 | 0.05186 | 0.01720 | 0.05036 | 9.750 |
| 9 | Stable-Tail-EdgeTail-a010 | 4.0355 | 1.1818 | 0.02850 | 0.05181 | 0.01695 | 0.05039 | 10.000 |
| 10 | Stable-Tail-TailOnly-a030 | 4.0307 | 1.1795 | 0.02855 | 0.05222 | 0.01729 | 0.05098 | 10.500 |
| 11 | Stable-Tail-EdgeTail-a030 | 4.0426 | 1.1805 | 0.02847 | 0.05192 | 0.01706 | 0.05160 | 10.750 |
| 12 | Stable-Tail-MatrixEns-r005 | 4.0404 | 1.1803 | 0.02871 | 0.05182 | 0.01699 | 0.05112 | 12.000 |
| 13 | Stable-Tail-NodeCalib-a005 | 4.0312 | 1.1807 | 0.02865 | 0.05207 | 0.01705 | 0.05109 | 12.000 |
| 14 | Stable-Tail-NodeCalib-a020 | 4.0333 | 1.1786 | 0.02867 | 0.05219 | 0.01678 | 0.05119 | 12.500 |
| 15 | Stable-Tail-EdgeTail-a005 | 4.0327 | 1.1806 | 0.02863 | 0.05224 | 0.01683 | 0.05058 | 13.000 |
| 16 | Stable-Tail-MatrixEns-r030 | 4.0416 | 1.1814 | 0.02865 | 0.05193 | 0.01689 | 0.05121 | 14.000 |
| 17 | Stable-Tail-TailOnly-a010 | 4.0444 | 1.1819 | 0.02862 | 0.05201 | 0.01693 | 0.05056 | 14.250 |
