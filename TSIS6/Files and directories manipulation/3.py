import os
def my_file(path):
    print("Test a path exists or not:")
    print(os.path.exists(path))
    print("\nFile name of the path:")
    print(os.path.basename(path))
    print("\nDir name of the path:")
    print(os.path.dirname(path))