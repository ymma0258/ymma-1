# Hazardous Materials Risk Experiments

This directory contains experiment planning notes and runnable utilities for the
hazardous materials transportation risk assessment study.

It is intentionally kept outside the PyVRP source tree. PyVRP is used only as a
downstream CVRP solver in later validation stages.

## Current contents

- `final_experiment_plan.md`: final innovation points and detailed experiment plan.
- `scripts/audit_hazmat_data.py`: reads the trajectory graph zip file and writes
  data audit reports.

## Data audit

Run from `D:\PyVRP-main`:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe .\hazmat_risk_experiments\scripts\audit_hazmat_data.py
```

Default input:

```text
D:\城市危险化学品运输车辆轨迹数据.zip
```

Default output directory:

```text
D:\PyVRP-main\hazmat_risk_experiments\outputs\audit
```

## Model smoke test

Run a single 1-epoch model smoke:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe .\hazmat_risk_experiments\scripts\train_risk_model.py --model teg_gnn --split A --epochs 1 --hidden-dim 32
```

Run a small batch smoke and aggregate results:

```powershell
.\PyVRP-main\.venv\Scripts\python.exe .\hazmat_risk_experiments\scripts\run_model_experiments.py --models mlp,gcn --splits A --seeds 0 --epochs 1 --hidden-dim 32 --batch-name smoke_batch
```

For formal experiments, increase `--epochs`, pass `--splits A,B,C`, and use
multiple seeds such as `--seeds 0,1,2,3,4`.
