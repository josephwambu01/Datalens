@echo off
title DataLens - Local Server
color 0A

echo.
echo  ==========================================
echo    DataLens - Starting Local Server...
echo  ==========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo  Python found. Starting server...
    echo.
    python start-server.py
    goto end
)

:: Try python3
python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo  Python found. Starting server...
    echo.
    python3 start-server.py
    goto end
)

:: Python not found
echo  ERROR: Python is not installed on this computer.
echo.
echo  To fix this:
echo  1. Go to https://www.python.org/downloads/
echo  2. Download and install Python (tick "Add to PATH")
echo  3. Restart your computer
echo  4. Double-click this file again
echo.
echo  -- OR --
echo.
echo  If you have Node.js installed, open Command Prompt
echo  in this folder and run:  npx serve .
echo.

:end
pause
