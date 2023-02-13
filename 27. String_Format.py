# 1.
 
animal = "dog"
item = "fench"

#print("The "+ animal+" jumps over the "+item)

# String format
#print("The {} jumps over the {}".format(animal,item))

print("The {0} jumps over the {1}".format(animal,item))  #Positional Arguments

print("The {animals} jumps over the {items}".format(animals="cat",items="gate"))    #keyword Arguments



# 2.

name = "Bishal"
print("Hello my name is {}".format(name))
print("hello {:10} Goodmorning.".format(name))
print("hello {:>10} Goodmorning.".format(name))
print("hello {:1<0} Goodmorning.".format(name))
print("hello {:^10} Goodmorning.".format(name))



# 3.
num = 3.14152
print("The number is Pi: {:.3f}".format(num))