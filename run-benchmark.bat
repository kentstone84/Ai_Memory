@echo off
REM TMC Benchmark Runner for Windows
REM Run this after starting the TMC server

echo ======================================
echo TMC Performance Benchmark
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.

REM Check if server is running
echo Checking if TMC server is running...
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: TMC server is not running on http://localhost:8000
    echo.
    echo Please start the server first using run-tmc-server.bat
    echo.
    pause
    exit /b 1
)

echo Server is running!
echo.

REM Install dependencies
echo Installing required packages...
pip install --quiet requests numpy 2>nul
echo.

REM Run benchmark
echo ======================================
echo Starting TMC Benchmark...
echo This will take approximately 2-3 minutes
echo ======================================
echo.

python benchmark_tmc.py

echo.
echo ======================================
echo Benchmark Complete!
echo ======================================
echo.
echo Results saved to benchmark_results.json
echo.
pause
