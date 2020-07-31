@echo on
REM This is a comment line. Replace next line with path to your mkdocs project directory
cd "C:\Users\<username>\my-project\"
echo "Current Directory:" %cd%
updatemkYAML.py

echo %ERRORLEVEL%
if %ERRORLEVEL% NEQ 0 (echo "Something went wrong with python call. Check for errors.") else mkdocs serve

PAUSE
