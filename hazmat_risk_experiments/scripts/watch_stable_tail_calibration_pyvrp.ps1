param(
    [int]$PollSeconds = 30,
    [int]$MaxRestarts = 10
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$experimentRoot = Join-Path $root "hazmat_risk_experiments"
$outputs = Join-Path $experimentRoot "outputs_10seed"
$python = Join-Path $root "PyVRP-main\.venv\Scripts\python.exe"
$pipeline = Join-Path $PSScriptRoot "run_10seed_pipeline.py"
$riskRoot = Join-Path $outputs "risk_matrices"
$pyvrpRoot = Join-Path $outputs "pyvrp_cvrp"
$finalSummary = Join-Path $pyvrpRoot "stable_tail_calibration_budget_sweep_10seed\calibration_summary.csv"
$failureFile = Join-Path $pyvrpRoot "stable_tail_calibration_pyvrp_10seed\model_pyvrp_failures.json"
$logDir = Join-Path $outputs "logs"
$logFile = Join-Path $logDir "stable_tail_calibration_pyvrp_watchdog.log"
$runLog = Join-Path $logDir "stable_tail_calibration_pyvrp_resume.log"

New-Item -ItemType Directory -Force -Path $logDir | Out-Null
Set-Location $root

function Write-WatchLog([string]$Message) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $logFile -Value "[$timestamp] $Message"
}

function Get-LatestRiskWriteTime {
    $latest = Get-ChildItem -LiteralPath $riskRoot -Recurse -Filter "calibration_meta.json" |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $latest) {
        throw "No calibration_meta.json files found under $riskRoot"
    }
    return $latest.LastWriteTime
}

function Test-FinalResultCurrent {
    if (-not (Test-Path -LiteralPath $finalSummary)) {
        return $false
    }
    if ((Get-Item -LiteralPath $finalSummary).LastWriteTime -le (Get-LatestRiskWriteTime)) {
        return $false
    }
    if (-not (Test-Path -LiteralPath $failureFile)) {
        return $false
    }
    return ((Get-Content -LiteralPath $failureFile -Raw).Trim() -eq "[]")
}

$restarts = 0
Write-WatchLog "Watchdog started."

while (-not (Test-FinalResultCurrent)) {
    $pythonRunning = @(Get-Process -Name "python" -ErrorAction SilentlyContinue).Count -gt 0
    if (-not $pythonRunning) {
        if ($restarts -ge $MaxRestarts) {
            Write-WatchLog "Maximum restart count reached; watchdog exiting."
            exit 2
        }
        $restarts += 1
        Write-WatchLog "No Python process found; resuming pipeline (attempt $restarts)."
        & $python -B $pipeline `
            --stages "stable_tail_calibration_pyvrp,stable_tail_calibration_budget_sweep" `
            --pyvrp-workers 8 *>> $runLog
        Write-WatchLog "Pipeline process returned with exit code $LASTEXITCODE."
    }
    Start-Sleep -Seconds $PollSeconds
}

Write-WatchLog "Fresh final calibration summary detected; watchdog exiting successfully."
