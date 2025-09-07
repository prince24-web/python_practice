class Animal:
    def __init__(self, name):
        self.name = name

    def speaks(self):
        print(f"{self.name} makes a sound")

class Dog(Animal): # Dog inherits from Animal
    def speaks(self): # override method
        print(f"{self.name} barks")

class Cat(Animal):
    def speaks(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
cat = Cat("whiskers")

dog.speaks()
cat.speaks()