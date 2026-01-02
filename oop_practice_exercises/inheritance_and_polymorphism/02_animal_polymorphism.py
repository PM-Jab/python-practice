class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"
    
mydog = Dog("Ben")
mycat = Cat("Niko")

for pet in [mydog, mycat]:
    print(pet.speak())

# Polymorphism allows different classes to be treated as the same type, even though they behave differently. The name literally means "many shapes."