class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")

mydog = Dog()
mydog.who_am_i()
mydog.bark()

# Inheritance allows one class (the Child) to take all the features and methods of another class (the Parent).