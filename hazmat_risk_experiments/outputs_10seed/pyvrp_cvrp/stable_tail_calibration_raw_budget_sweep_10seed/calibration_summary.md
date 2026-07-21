# Stable-Tail post-processing calibration

All metrics are lower-is-better; AUBRC uses trapezoidal integration over B=10%--40%.

| Rank | Calibration | Avg Risk@B | Common AUBRC | CVaR90 | CVaR95 | LoadCVaR90 | MaxVehCVaR90 | Core score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Stable-Tail-TailOnlyRaw-a030 | 3.9722 | 1.1622 | 0.02801 | 0.05101 | 0.01674 | 0.04993 | 1.000 |
| 2 | Stable-Tail-MatrixEnsRaw-r040 | 4.0050 | 1.1707 | 0.02825 | 0.05132 | 0.01683 | 0.05058 | 2.750 |
| 3 | Stable-Tail-EdgeTailRaw-a005 | 4.0119 | 1.1727 | 0.02825 | 0.05120 | 0.01698 | 0.05066 | 3.500 |
| 4 | Stable-Tail-EdgeTailRaw-a030 | 4.0081 | 1.1730 | 0.02827 | 0.05141 | 0.01677 | 0.04951 | 4.500 |
| 5 | Stable-Tail-NodeCalibRaw-a005 | 4.0116 | 1.1723 | 0.02829 | 0.05145 | 0.01675 | 0.05083 | 4.750 |
| 6 | Stable-Tail-TailOnlyRaw-a020 | 4.0189 | 1.1750 | 0.02816 | 0.05154 | 0.01693 | 0.05037 | 6.250 |
| 7 | Stable-Tail-EdgeTailRaw-a010 | 4.0243 | 1.1737 | 0.02838 | 0.05140 | 0.01689 | 0.05054 | 6.750 |
| 8 | Stable-Tail-EdgeTailRaw-a020 | 4.0136 | 1.1739 | 0.02838 | 0.05149 | 0.01703 | 0.05028 | 7.000 |
| 9 | Stable-Tail-TailOnlyRaw-a010 | 4.0223 | 1.1761 | 0.02850 | 0.05158 | 0.01685 | 0.05050 | 9.250 |
| 10 | Stable-Tail-MatrixEnsRaw-r020 | 4.0193 | 1.1751 | 0.02858 | 0.05196 | 0.01676 | 0.05086 | 9.750 |
| 11 | Stable-Tail-MatrixEnsRaw-r010 | 4.0375 | 1.1795 | 0.02851 | 0.05202 | 0.01693 | 0.05168 | 11.250 |
| 12 | Stable-Tail-NodeCalibRaw-a010 | 4.0444 | 1.1826 | 0.02861 | 0.05188 | 0.01696 | 0.05119 | 13.000 |
| 13 | Stable-Tail-MatrixEnsRaw-r005 | 4.0332 | 1.1803 | 0.02874 | 0.05220 | 0.01706 | 0.05148 | 13.250 |
| 14 | Stable-Tail-NodeCalibRaw-a030 | 4.0400 | 1.1813 | 0.02866 | 0.05204 | 0.01699 | 0.05180 | 13.250 |
| 15 | Stable-Tail-MatrixEnsRaw-r030 | 4.0444 | 1.1834 | 0.02858 | 0.05233 | 0.01714 | 0.05087 | 14.500 |
| 16 | Stable-Tail-NodeCalibRaw-a020 | 4.0474 | 1.1855 | 0.02879 | 0.05217 | 0.01703 | 0.05073 | 16.000 |
| 17 | Stable-Tail-TailOnlyRaw-a005 | 4.0479 | 1.1852 | 0.02875 | 0.05225 | 0.01717 | 0.05088 | 16.250 |
