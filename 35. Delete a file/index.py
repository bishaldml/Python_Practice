import os, shutil

path = "C:\\python_projects\\Python_Practice\\35. Delete a file\\folder"
 
try: 
    #os.remove(path) #delete a file
    os.rmdir(path)  #delete an empty folder
    #shutil.rmtree(path) #delete a folder containing file

except FileNotFoundError:
    print('file not found')
except PermissionError:
    print('you donot have permission to delete')
except OSError:
    print("you cannot delete using that function")
else:
    print(path +" was deleted")