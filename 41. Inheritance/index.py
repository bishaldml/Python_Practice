class Animal:   #Parent class

    alive = True

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal):  #child class
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    def fly():
        print("This hawk is flying.")

rabbit = Rabbit()   #defining objects
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()

