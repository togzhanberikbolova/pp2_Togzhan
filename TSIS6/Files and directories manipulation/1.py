import os
def list_dir_fil(path):
    print("only directories: ")
    print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
    print("\nonly files: ")
    print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
    print("\nall directories and files")
    print([ name for name in os.listdir(path) ])

list_dir_fil("C:\Users\user\pp2_Togzhan")

