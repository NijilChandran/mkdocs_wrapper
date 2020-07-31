import os
from yaml import dump

site_name  = "Your site name goes here"
theme_dict = { "name": "readthedocs" , "include_sidebar": True, "navigation_depth": 10 }
yml_filename ="/mkdocs.yml"
mdfolder="/docs"

def updateYAML():

    cwd = os.getcwd()
    os.chdir(cwd+mdfolder)
    files = os.listdir()
    list_files = [f for f in files if f.endswith(".md") ]
   
    if(os.path.isfile(cwd+yml_filename)):
        print("Deleting exist .yml file...")
        os.remove(cwd+yml_filename)

    nav_list=[]
    for k in list_files:
        nav_list.append({k.split(".")[0]:k})

    main_dict  = { "site_name":site_name,"nav":nav_list,"theme":theme_dict }
   
    with open(cwd+yml_filename, 'w') as file:
        documents = dump(main_dict, file)

    print(yml_filename+ " file created succesfully.")  

if __name__ == '__main__':
    updateYAML()  
