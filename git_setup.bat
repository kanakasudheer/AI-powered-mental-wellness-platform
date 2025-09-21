@echo off
echo Setting up Git repository for MitraMind...

REM Initialize Git repository
git init

REM Add all files (excluding .env due to .gitignore)
git add .

REM Create initial commit
git commit -m "Initial commit: MitraMind AI Mental Wellness Companion"

echo.
echo Git repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub named 'mitramind'
echo 2. Run: git remote add origin https://github.com/yourusername/mitramind.git
echo 3. Run: git branch -M main
echo 4. Run: git push -u origin main
echo.
pause