@echo off
echo Starting MitraMind Chatbot...
echo.
cd /d "%~dp0"
python -m streamlit run streamlit_app.py
pause