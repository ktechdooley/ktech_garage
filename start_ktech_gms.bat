@echo off
title kTech Garage Management System

echo =====================================
echo   kTech Garage Management System
echo =====================================
echo.

REM Change to script directory
cd /d %~dp0

REM Activate virtual environment
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found.
    echo Please create it first using:
    echo   python -m venv .venv
    pause
    exit /b
)

call .venv\Scripts\activate.bat

echo Virtual environment activated.
echo Starting application...
echo.

REM Start the app
python run.py

echo.
echo Application stopped.
pause
