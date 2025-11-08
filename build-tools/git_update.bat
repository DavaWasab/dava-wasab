@echo off
echo Updating GitHub repository...
cd ..
git add .
git commit -m "Update: %date% %time%"
git push
echo.
echo Done! Changes pushed to GitHub
pause
