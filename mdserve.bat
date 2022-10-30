@echo on
REM Comment lines starts with REM. 

REM Replace next line with path to your mkdocs project directory.
set mkdocs_project_dir="C:\Users\Nijil\Documents\my-project"

REM Use anaconda .bat path if required. Comment the next line if using python directly
set conda_path="C:\Users\Nijil\Anaconda3\Scripts\activate.bat"

echo "mkdocs project directory:" %mkdocs_project_dir%

call %conda_path%
python updatemkYAML.py %mkdocs_project_dir%

cd /D %mkdocs_project_dir%
echo "Call mkdocs serve if return code is 0. Return code value: " %ERRORLEVEL%
if %ERRORLEVEL% NEQ 0 (echo "Something went wrong with python call. Check for errors.") else mkdocs serve

PAUSE
