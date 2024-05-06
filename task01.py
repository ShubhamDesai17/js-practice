import os
# folder=input("enter folder names: ").
# for dir in folder:
#     files=os.listdir(dir)

folders=input("Enter folder names with space in between: ").split()
for folder in folders:
    try:
        file= os.listdir(folder)
    except FileNotFoundError:
        print("Please enter valid file name")
        break
    except PermissionError:
        print("you dont have enough permission to access this folder")
    for f in file:
        print(f)
    print("_______________________________________")
