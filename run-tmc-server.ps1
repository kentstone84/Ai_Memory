# TMC Server Launcher for Windows (PowerShell)
# Place this file in the same directory as tmc-server.exe

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "TMC Server - Starting..." -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Set your license key
$env:TMC_LICENSE_KEY = "eyJjdXN0b21lciI6ICJrZW50LnN0b25lQGdtYWlsLmNvbSIsICJleHBpcmVzIjogMTc5ODI5MTUyNSwgImlzc3VlZCI6IDE3NjY3NTU1MjUsICJ0aWVyIjogImVudGVycHJpc2UifXx90BKKLZhdy4cmmHIFQ3m+9BFm+oB7pJ/IzHZREHlqEw=="

Write-Host "License: Enterprise" -ForegroundColor Green
Write-Host "Customer: kent.stone@gmail.com" -ForegroundColor Green
Write-Host "Expires: 2026-12-26" -ForegroundColor Green
Write-Host ""

# Start the server
.\tmc-server.exe

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Server stopped. Press any key to exit." -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Read-Host
