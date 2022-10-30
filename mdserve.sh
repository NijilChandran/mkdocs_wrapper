# mkdocs_project_dir should have the base path of your mkdocs project.
# Create a directory named 'docs' under the base path. Place all the .md files inside 'docs' folder
# Replace value of mkdocs_project_dir variable 
export mkdocs_project_dir="/root/project/"
echo "mkdocs project directory: $mkdocs_project_dir"
python3 updatemkYAML.py $mkdocs_project_dir
cd $mkdocs_project_dir
mkdocs serve