student = ("ram",22,"Male","Male")

print(student.index("ram"))
print(student.count("Male"))

for i in student:
    print(i)

if "ram" in student:
    print("Hello ram!") 