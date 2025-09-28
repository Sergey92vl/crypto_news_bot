@echo off
chcp 65001 > nul
echo ========================================
echo      Crypto News AI Bot by Gavanni Puerto (m1st1k)
echo ========================================
echo.

REM Checking if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or added to the PATH.
    echo Please install Python from the python.org website.
    pause
    exit /b 1
)

REM Checking whether the argument has been passed
if "%~1"=="" (
    set /p "query=Enter your request about the cryptoproject: "
) else (
    set "query=%*"
)

REM Run the Python script by passing it a request
python news_bot.py "%query%"

echo.
echo The search is completed.
pause