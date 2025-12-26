@echo off
REM TMC Server Launcher for Windows
REM Place this file in the same directory as tmc-server.exe

echo ======================================
echo TMC Server - Starting...
echo ======================================
echo.

REM Set your license key
set TMC_LICENSE_KEY=eyJjdXN0b21lciI6ICJrZW50LnN0b25lQGdtYWlsLmNvbSIsICJleHBpcmVzIjogMTc5ODI5MTUyNSwgImlzc3VlZCI6IDE3NjY3NTU1MjUsICJ0aWVyIjogImVudGVycHJpc2UifXx90BKKLZhdy4cmmHIFQ3m+9BFm+oB7pJ/IzHZREHlqEw==

REM Start the server
tmc-server.exe

echo.
echo ======================================
echo Server stopped. Press any key to exit.
echo ======================================
pause
