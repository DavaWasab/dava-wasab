@echo off
echo Initializing Git repository...
cd ..
git init
git add .
git commit -m "Initial commit: DavaWasab Portfolio"
git branch -M main
git remote add origin https://github.com/DavaWasab/dava-wasab.git
echo.
echo Done! Now run git_push.bat to upload to GitHub
pause
