age = int(input("How old are you: "))

if age == 100 or age > 100:
    print("You are century year old.")

elif age < 18 and age > 0:
    print("You are a child.")

elif age >= 18 and age < 100:
    print("You are an adult.")

else:
    print("You are not born yet.")