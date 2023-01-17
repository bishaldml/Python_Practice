# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)

# Above Program using not operator

name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name)