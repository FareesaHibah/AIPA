import os
### CREATING A FOLDER ###


# direc=("AIPA")
# try:
#     os.makedirs(direc)
#     print("Folder created:",direc)
# except FileExistsError:
#     print("Folder already exists.")
# finally:
#     print("Code is executed!")


### RENAMING A FOLDER ###
# cur_name="AI"
# new_name="AIPA"
# try:
#     os.rename(cur_name,new_name)
#     print("Folder renamed as: ",new_name)
# except FileNotFoundError:
#     print("File coud not be found.")

# import shutil

# del_dir="AIPA"
# try:
#     shutil.rmtree(del_dir)   ### FUNCTION OF A DIRECTORY WHICH WILL DELETE THE CONTENT OF THE FOLDER. ###
#     print("Directory deleted.")
# except PermissionError:
#     print("Permission denied!")
# except Exception as e:
#     print("An error occurred.",e)

import os

# dir="AIPA"
# try:
#     os.makedirs(dir,exist_ok=True)
#     file_name="nsti.txt"
#     file_path=os.path.join(dir,file_name)
#     with open(file_path,"w") as file:
#         file.write("Hello! Have a good day!")
#         print(f"File: {file_name} created successfully in {dir}")
# except Exception as e:
#     print("An error occurred: ",e)

### LIST THE THINGS IN THE FOLDER ###
# dir="."    ### GIVES THE PATH OF THE CURRENT DIRECTORY ###
# with os.scandir(dir) as entries:
#     print("Contents of the folder are: ",dir)
#     for entry in entries:
#         print(entry.name)

# dir=os.listdir()
# print("Contents of folder are: ",dir)

### TO VIEW THE FOLDER YOU'RE CURRENTLY WORKING IN ###
# dir=os.getcwd()
# print("You're currently working in: ",dir)

# import shutil
# dir="AIPA"
# x="AIPA_copy"
# shutil.copytree(dir,x)
# print("Folder copied.")

# shutil.move(dir,x)
# print("Folder moved.")

