def names(**kwargs):
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

names(fn="Bishal",mn="Bahadur",ln="Dhimal")
    