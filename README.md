# mkdocs_wrapper
View markdown files on a browser with one click. Wrapper for mkdocs
Tested only on Windows. Might need minor tweeks to make it work on \*nix based OS.

[Mkdocs](https://www.mkdocs.org/) renders all your markdown (.md) files on a browser.   
This wrapper for mkdocs does two things that can simplify how you use mkdocs on a windows computer.

## Why do I need this wrapper?

- Mkdocs is fantastic, but everytime you need to see the .md files on your browser, you need to open a terminal,
  go to the project directory and execute a command to serve it up.   
- Instead this wrapper will do all that with a click of a shortcut that you can keep on your desktop.  
- This will also update the mkdocs.yml file with all the latest .md files
  in your "docs" directory, you don't have to worry about adding them manually anymore. 

## Steps

- Install [Mkdocs](https://www.mkdocs.org/) on your computer.
- Clone or download mkdocs_wrapper project to your computer.
- Modify the variable mkdocs_project_dir in the mdserve.bat file from mkdocs_wrapper.
  + mkdocs_project_dir is the path to the mkdocs project in your computer.
- Create a shortcut pointing to mdserve.bat file on your desktop. Or you can just click on the .bat file.
- Click on the shortcut anytime you want the files to start up mkdocs.

## Python installed via Anaconda package manager

- Add a call to conda in MkdocsServe.bat before the python call  
     *call [Replace Path to conda.bat] activate base*
- This will invoke default conda environment (base) instead of looking up for Python installation in the Windows PATH
- To know your conda.bat path ,  execute *where conda* on your Anaconda terminal
- Path to conda.bat should look something like:  
  C:\Users\<username>\Anaconda3\Library\bin\conda.bat 

## updatemkYAML.py

- Deletes the existing mkdocs.yml file at the my-project directory
- Gets a list of all the .md file in your "docs" folder and creates a new mkdocs.yml file
- Themes or other new changes that you want on the mkdocs.yml file lives on updatemkYAML.py

## mdserve.bat

- Changes directory to the location of my-project. Make changes according to your local path
- Calls updateYAML.py to create a new mkdocs.yml that will have all the .md files in your list
- calls mkdocs serve to serve the markdown files at http://127.0.0.1:8000
