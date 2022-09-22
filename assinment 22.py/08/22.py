#1.create a credit card class with the following attributes: card number, expiration date, and security code. Create a method that will print out the card number, expiration date, and security code. Create an instance of the class and call the method.
from random import randint
class Credit_card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_card = security_code
    def cd (self):
        return self.card_number
    def exp(self):
        return self.expiration_date 
    def sc (self):
        return self.security_card

Tom = Credit_card(randint(1000000000, 10000000000), "31/12/2030", randint(0000, 10000))
print(f"Card number :{Tom.cd()} \n Expiry date:{Tom.exp()} \n Security code: {Tom.sc()}")


#2.create Animal class and Dog class. Make the Dog class inherit from the Animal class. Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
    def bark(self):
        return "Whoof Whoof"
one = Dog("Lucas", "German Shepherd")
print(one.bark())


##3.create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. The size method should return the size of the queue.
class Queue:
    def __init__(self, element, lst, size):
        self.element = element
        self.lst = lst
        self.size = size
    def dequeue(self):
        if len(self.lst) != 0:
            self.lst.pop()
            return self.lst
        else:
            return 'The list is already empty'

    def length(self):
        return len(self.lst)

    def enqueue(self,element):
        if len(self.lst) < self.size:
            self.lst.insert(0,self.element)
            return self.lst
        else:
            return "list is full"
# 4.create a class called Stack. The class should have the following methods: push, pop, and size. The push method should add an item to the stack. The pop method should remove an item from the stack. The size method should return the size of the stack.
class Stack:
    def __init__(self, item, lst, length):
        self.item = item
        self.length = length    
   
    def pop(self):
        if len(self.lst) != 0:
           self.lst.pop(-1)
           return self.lst
        else:
            return 'The list is already empty'

    def size(self):
        return len(self.lst)

    def push(self,item):
        if len(self.lst) < self.length:
            self.lst.insert(0,self.item)
            return self.lst
        else:
            return "list is full"

#5.create a class called Person. The class should have the following attributes: name, age, and address. The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". The work method should print out the name of the person and the word "is working"
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self. age = age
        self.address = address
    def eat(self, name):
       return f"{self.name} is eating"
    def sleep(self, name):
        return f"{self.name} is sleeping"
    def work(self, name):
        return f"{self.name} is working"


#6.create a class called Employee. The class should have the following attributes: name, age, and salary. The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". The work method should print out the name of the person and the word "is working". Create a subclass of Employee called Programmer. The Programmer class should have the following attributes: name, age, salary, and programming language. The Programmer class should have the following methods: eat, sleep, work, and code. The code method should print out the name of the person and the word "is coding in" and the programming language. Create an instance of the Programmer class and call all the methods.
class Employee():
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def eat(self, name):
        return f"{self.name} is eating"
    def sleep(self, name):
        return f"{self.name} is sleeping"
    def work(self, name):
        return f"{self.name} is working"

class Programmer(Employee):
    def __init__(self,name, age, salary, programming_language):
        self.programming_language = programming_language
        super(). __init__(name, age, salary)

    def code(self,name, programming_language ):
        return f"{self.name} is coding in {self.programming_language}"
two = Programmer("Mary", 12, 10000000000, "Python")
print(two.eat("Mary"))
print(two.sleep("Mary"))
print(two.work("Mary"))
print(two.code("Mary", "Python"))


#7 create a class called Vehicle. The class should have the following attributes: make, model, and year. The class should have the following methods: start, stop, and drive. The start method should print out the make, model, and year of the vehicle and the word "is starting". The stop method should print out the make, model, and year of the vehicle and the word "is stopping". The drive method should print out the make, model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle called Car. The Car class should have the following attributes: make, model, year, and color. The Car class should have the following methods: start, stop, drive, and park. The park method should print out the make, model, year, and color of the car and the word "is parking". Create an instance of the Car class and call all the methods.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self. model = model
        self. year = year

    def start(self, make, model, year):
        return f"{self.make} {self.model} {self.year} is starting."
    def stop(self, make, model, year):
        return f"{self.make} {self.model} {self.year} is stopping."
    def drive(self, make, model, year):
        return f"{self.make} {self.model} {self.year} is driving."

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.color = color
        super(). __init__(make, model, year)
    def park(self, make, model, year, color):
        return f"{self.make} {self.model} {self.year} {self.color} is parking."

four = Car("BMW", "X5", 2019, "purple")
print(four.stop("BMW","X5",2019, ))
print(four.start("BMW","X5",2019, ))
print(four.drive("BMW","X5",2019, ))
print(four.park("BMW","X5",2019,"purple" ))


#8.create a class called Animal. The class should have the following attributes: name, color, and age. The class should have the following methods: eat, sleep, and make_sound. The eat method should print out the name of the animal and the word "is eating". The sleep method should print out the name of the animal and the word "is sleeping". The make_sound method should print out the name of the animal and the word "is making a sound". Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and breed. The Dog class should have the following methods: eat, sleep, make_sound, and bark. The bark method should print out the name of the dog and the word "is barking". Create an instance of the Dog class and call all the methods.
class Animal:
    def __init__(self,name, color, age):
        self.name =  name
        self.color = color
        self.age = age
    def eat(self, name):
        return f"{self.name} is eating." 
    def sleep(self, name):
        return f"{self.name} is sleeping."
    def make_sound(self, name):
        return f"{self.name} is making a sound."

class Dog(Animal):
    def __init__(self,name, color, age, breed):
        self.breed = breed
        super(). __init__(name, color, age)
    def bark(self, name):
        return f"{self.name} is barking"
five = Dog("Mercy", "brown", 3, "German Shepherd")
print(five.eat("Mercy"))
print(five.sleep("Mercy"))
print(five.make_sound("Mercy"))
print(five.bark("Mercy"))

#9.create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. Implement polymorphism, encapsulation, and inheritance.
class Choice:
    def __init__(self, item, name, location):
        self.__max = 900
        self.item = item
        self.name = name
        self.location = location
    def number(self, item):
        return f"This is item number {self.item}"
    def called(self, name):
        return f"This item is called {self.name}"
    def found(self,location):
        return f"This item can be found in {self.location}"
    def setMax(self,price):
        self.__max = price
    def getMax(self):
        return self.__max

class Map(Choice):
    def __init__(self, item, name, location):
        super(). __init__(item, name, location)
    def direction(self):
        return "North"
class Google(Choice):
    def __init__(self, item, name, location):
        super(). __init__(item, name, location)
    def direction(self):
        return "North East"
def campus(source):
    source.direction()
one = Map(1,"L.Victoria", "Uganda")
two = Google(2, "Kampala", "Kenya")
campus(one)
campus(two)

    