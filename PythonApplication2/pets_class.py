# Parent class
class Pets:
    dogs=[]
    def __init__(self, dogs):
        self.dogs=dogs
class Dog:

    # Class attribute
    species = 'mammal'
    color="white"
    
    

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry=True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
       

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    def eat(self):
        self.is_hungry=False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
        color="Black"
        species="not a mammal"
        def run(self, speed):
        
            return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        
        return "{} runs {}".format(self.name, speed)

my_dogs=[Bulldog("Tom",6), RussellTerrier("Fletcher",7),Dog("Larry",9)]

my_pets=Pets(my_dogs)
print("I have {} dogs".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {} and color is {}".format(dog.name, dog.age, dog.color))
print("And they are all {} off course".format(dog.species))
are_my_dogs_hungry=False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry=True
if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
#for dog in my_pets.dogs:
 #   print(dog.color)
d=RussellTerrier
print(d.color)
