import os,sys
from yaml import dump

site_name  = "Your site name"
theme_dict = { "name": "readthedocs" , "include_sidebar": True, "navigation_depth": 10 }
yml_filename ="/mkdocs.yml"
mdfolder='/docs'

def updateYAML():
    
    try:
        cwd = os.path.normpath(sys.argv[1])
        if(os.path.isfile(cwd+yml_filename)):
            print("Deleting existing .yml file...")
            os.remove(cwd+yml_filename)
        os.chdir(cwd+mdfolder)
        files = os.listdir()
    except IndexError:
        print("mkdocs project path is not passed as argument to this program.")
        exit(-1)
    except FileNotFoundError:
        print("mkdocs project directory passed to this program doesn't exist ")
        exit(-2)
    except OSError:
        print("The filename, directory name, or volume label syntax is incorrect"+sys.argv[1])
        print("Try removing the \ at the end of the mkdocs project directory passed to this program")
        exit(-3)

    list_files = [f for f in files if f.endswith(".md") ]
    print("list_files ",list_files)
    nav_list=[]
    for k in list_files:
        nav_list.append({k.split(".")[0]:k})

    main_dict  = { "site_name":site_name,"nav":nav_list,"theme":theme_dict }
   
    with open(cwd+yml_filename, 'w') as file:
        documents = dump(main_dict, file)

    print(yml_filename+ " file created succesfully.")  

if __name__ == '__main__':
    updateYAML()  
