@echo off
echo ========================================
echo   DavaWasab Portfolio - Deploy Tool
echo ========================================
echo.
echo Choose action:
echo 1. First time setup (init git + push)
echo 2. Update site (commit + push)
echo 3. Update galleries only
echo 4. Start local server
echo 5. Rename images by date
echo.
set /p choice="Enter number (1-5): "

if "%choice%"=="1" goto init
if "%choice%"=="2" goto update
if "%choice%"=="3" goto galleries
if "%choice%"=="4" goto server
if "%choice%"=="5" goto rename
goto end

:init
echo.
echo Initializing Git repository...
cd ..
git init
git add .
git commit -m "Initial commit: DavaWasab Portfolio"
git branch -M main
git remote add origin https://github.com/DavaWasab/dava-wasab.git
git push -u origin main
echo.
echo Done! Site will be at: https://davawasab.github.io/dava-wasab
goto end

:update
echo.
echo Updating GitHub repository...
cd ..
git add .
git commit -m "Update: %date% %time%"
git push
echo.
echo Done! Changes pushed to GitHub
goto end

:galleries
echo.
echo Updating galleries...
python generate_galleries.py
echo.
echo Done!
goto end

:server
echo.
echo Starting local server at http://localhost:8000
echo Press Ctrl+C to stop
echo.
cd ..
python -m http.server 8000
goto end

:rename
echo.
echo Renaming images by creation date...
python rename_images_by_date.py
echo.
echo Done! Run option 3 to update galleries
goto end

:end
echo.
pause
