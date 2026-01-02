class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

mydog = Dog("Tim")
mycat = Cat("Felix")

for pet in [mydog, mycat]:
    print(pet.speak())