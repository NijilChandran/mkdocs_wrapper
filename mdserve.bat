@echo off
REM This is a comment line. Replace next line with path to your mkdocs project directory.
set mkdocs_project_dir="C:\Users\Nijil\Documents\my-project"
cd %mkdocs_project_dir%
echo "mkdocs project directory:" %mkdocs_project_dir%
Python updatemkYAML.py %mkdocs_project_dir%

echo "Returncode from python call" %ERRORLEVEL%
if %ERRORLEVEL% NEQ 0 (echo "Something went wrong with python call. Check for errors.") else mkdocs serve

PAUSE
