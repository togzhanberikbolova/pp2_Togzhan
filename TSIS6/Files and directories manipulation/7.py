import os
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source, open(destination_path, 'w') as dest:
        dest.write(source.read())
