# TMC Benchmark Runner for Windows (PowerShell)
# Run this after starting the TMC server

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "TMC Performance Benchmark" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
    Write-Host ""
}
catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if server is running
Write-Host "Checking if TMC server is running..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -TimeoutSec 2 -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "Server is running!" -ForegroundColor Green
        Write-Host ""
    }
}
catch {
    Write-Host ""
    Write-Host "ERROR: TMC server is not running on http://localhost:8000" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please start the server first using:" -ForegroundColor Yellow
    Write-Host "  .\run-tmc-server.ps1" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Install dependencies
Write-Host "Installing required packages..." -ForegroundColor Yellow
pip install --quiet requests numpy 2>$null
Write-Host "Dependencies installed!" -ForegroundColor Green
Write-Host ""

# Run benchmark
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Starting TMC Benchmark..." -ForegroundColor Cyan
Write-Host "This will take approximately 2-3 minutes" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

python benchmark_tmc.py

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Benchmark Complete!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Results saved to benchmark_results.json" -ForegroundColor Green
Write-Host ""
Read-Host "Press Enter to exit"
