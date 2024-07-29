REM This test scripts aims to be called in each repo. It tests everything to fit as much as possible whats in Tekton
@echo off
call cd ..
setlocal enabledelayedexpansion
for %%I in (.) do set "folder_name=%%~nxI"
set mainfoldername=%1
title %folder_name% tests

for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"') do set "start_time=%%a"
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_PYLINT=%current_time%
echo ===================================================== [%current_time%] Starting tests for %folder_name% =======================================================

call "%CD%\..\..\sostrades-venv\Scripts\activate"
echo venv (sostrades-venv) activated successfuly

set "strategy_test_file=%CD%\..\..\platform\sostrades-core\sostrades_core\tests\strategy.py"

set "pylint_status=Passed"
set "ruff_status=Passed"
set "pytest_l0_status=Passed"
set "pytest_l1_status=Passed"
set "pytest_usecases_status=Passed"

for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_PYLINT=%current_time%
echo.
echo ****************************************************************************************************
echo ****************************************************************************************************
echo *********************************  [%current_time%]
echo *********************************  Running pylint ...
echo *********************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo.
call pylint --disable=E1101 --jobs=0 --errors-only %mainfoldername%
if %errorlevel% neq 0 set "pylint_status=Failed"

REM Execute "ruff check" in current directory
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_RUFF=%current_time%
echo.
echo ****************************************************************************************************
echo ****************************************************************************************************
echo *********************************  [%current_time%]
echo *********************************  Running ruff ...
echo *********************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo.
ruff check .
if %errorlevel% neq 0 set "ruff_status=Failed"
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_L0=%current_time%
REM Run all python tests with pytest for files starting with l0_*.py in mainfoldername\tests
echo.
echo ****************************************************************************************************
echo ****************************************************************************************************
echo *********************************  [%current_time%]
echo *********************************  Running L0...
echo *********************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo.
call python %strategy_test_file% %mainfoldername% l0
if %errorlevel% neq 0 set "pytest_l0_status=Failed"
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_L1=%current_time%

echo.
echo ****************************************************************************************************
echo ****************************************************************************************************
echo *********************************  [%current_time%]
echo *********************************  Running L1...
echo *********************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo.
call python %strategy_test_file% %mainfoldername% l1
if %errorlevel% neq 0 set "pytest_l1_status=Failed"

for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
set CT_UC=%current_time%
echo.
echo ****************************************************************************************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo *********************************  [%current_time%]
echo *********************************  Running usecases ... 
echo *********************************
echo ****************************************************************************************************
echo ****************************************************************************************************
echo.
call python %strategy_test_file% %mainfoldername% uc
if %errorlevel% neq 0 set "pytest_usecases_status=Failed"

echo.
echo Script execution completed.
echo.
echo Summary:
echo --------
echo [%CT_PYLINT%] Pylint: %pylint_status%
echo [%CT_RUFF%] Ruff: %ruff_status%
echo [%CT_L0%] Pytest L0: %pytest_l0_status%
echo [%CT_L1%] Pytest L1: %pytest_l1_status%
echo [%CT_UC%] Pytest Usecases: %pytest_usecases_status%
echo Header test not checked : check on your own !
echo.

for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'HH:mm:ss'"') do set "current_time=%%a"
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"') do set "end_time=%%a"

set "ps_command="
set "ps_command=%ps_command% $start = [datetime]::ParseExact('%start_time%', 'yyyy-MM-dd HH:mm:ss', $null);"
set "ps_command=%ps_command% $end = [datetime]::ParseExact('%end_time%', 'yyyy-MM-dd HH:mm:ss', $null);"
set "ps_command=%ps_command% $duration = $end - $start;"
set "ps_command=%ps_command% $minutes = [math]::Floor($duration.TotalMinutes);"
set "ps_command=%ps_command% $seconds = $duration.Seconds;"
set "ps_command=%ps_command% '{0}:{1:D2}' -f $minutes, $seconds"

for /f "delims=" %%a in ('powershell -Command "%ps_command%"') do set "duration=%%a"


echo ===================================================== [%current_time%] End of tests (duration %duration%) =======================================================

pause
pause

