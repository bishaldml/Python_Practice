import os
source = "C:\\Users\\Lenovo\\Desktop\\folder"
destination = "C:\\python_projects\\Python_Practice\\34. Move_a_file\\folder"

try:
    if os.path.exists(destination):
        print('there is already a file there.')
    else: 
        os.replace(source,destination)
        print(source +" was moved.")
except FileNotFoundError:
    print(source +" was not found.")
