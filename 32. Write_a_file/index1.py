text = " \n See you tommorrow bye bye..."
path = "C:\\python_projects\\Python_Practice\\32. Write a file\\test.txt"
with open(path,'a') as file:
    print(file.write(text))