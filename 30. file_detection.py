import os 

path = "C:\\Users\\Lenovo\\Desktop\\file.txt"
path1 = "C:\\Users\\Lenovo\\Desktop\\folder"
if os.path.exists(path):
    print("That location exits.")
    if os.path.isfile(path):
        print("It is a file.")
else:
    print("That location doesnot exits.")