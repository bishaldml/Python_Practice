# Break Example

while True: 
    name = input("Enter your name : ")
    if name != "":
        break


# Continue Example

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")


# Pass Example
for i in range(1,11):
    if i == 5:
        pass
    else:
        print(i)