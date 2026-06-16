@echo off
title Supplement Watcher
echo ============================================
echo   Supplement Auto-Watcher
echo   Ko oznacis Vyvanse ali Vecerja v Obsidianu,
echo   se vsi odvisni teski avtomatsko posodobijo.
echo ============================================
echo.

:: Preveri ce je pip/watchdog instaliran
python -c "import watchdog" 2>nul
if errorlevel 1 (
    echo Instaliram watchdog...
    pip install watchdog --break-system-packages -q
)

:: Zazeni watcher
python "%~dp0supplement_watcher.py"
pause
