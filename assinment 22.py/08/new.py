class Animal:
    def __init__(self,name, color, type, age):
        self.color = color
        self.type = type
        self.age = age
        self.name = name
    def what_color(self, name, color):
        return(f"My {self.name} is {self.color}.")

    def what_type(self, type, name):
        return(f"{self.name} is a {self.type}.")

    def what_age(self, name, age):
        return(f"{self.name} is {self.age} years old.")
#inheritance
class Dog(Animal):
    def __init__(self,name, color, type, age):
        super().__init__(name, color, type, age)
    def loyalty(self):
        return ("Is very loyal ")
one = Dog("Chris","brown", "Dog", 5)
#print(one.name, one.color, one.type, one.age)

print(one.what_age('Chris',5))
print(one.what_color("Chris", "Brown"))
print(one.what_type("Dog", "Chris"))
print("\n")
class Cat(Animal):
    def __init__(self,name, color, type, age):
        super().__init__(name, color, type, age)
    def sound(self):
        return("Makes the sound meow")

two = Cat("Anna", "White", "cat", 3)
print(two.what_age('Anna',3))
print(two.what_color("Anna", "  white"))
print(two.what_type("Cat", "Anna"))
print("\n")

#multi inheritance
class CatDog(Dog, Cat):
    def __init__(self,name, color, type, age):
        super().__init__(name, color, type, age)

three = CatDog("Morris","Grey", "CatDog", 1 )
print(three.what_age('Morris',1))
print(three.what_color("Morris", "Grey"))
print(three.what_type("CatDog", "Morris"))
print(three.loyalty())
print(three.sound())




