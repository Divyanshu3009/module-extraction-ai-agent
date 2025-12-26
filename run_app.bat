@echo off
echo ==========================================
echo Module Extraction AI Agent - Setup
echo ==========================================

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.9+ from https://www.python.org
    pause
    exit /b
)

echo Python found.

echo Installing required libraries...
pip install -r requirements.txt

echo Starting Streamlit application...
streamlit run app.py

pause
