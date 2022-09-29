#1.Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.
#class Animals:
    #def __init__(self,name,age,food):
       # self.name=name
      #  self.age = age
     #   self.food = []
    #def get_name(self):
     #   self.name = input(" What is the animal's name?")
    #def set_name(self):
     #   return f"Animal's name is {self.name}"
    #def get_age(self):
     #   self.age = int(input(" What is the animal's age?"))
    #def set_age(self):
     #   return f"Animal's age is {self.age}"
    #def get_food(self):
     #   self.food = input("Enter food item:")
    #def add_food(self, food):
   #     self.food.append(self.food)
  #  def remove_food(self,food):
 #       self.food.pop(self.food)
#class Cat(Animals):
    #def __init__(self,name,age,food):
   #     super().__init__(name, age,food)
  #  def talk(self):
 #       return "Meow"
#class Fish(Animals):
    #def __init__(self,name,age,food):
   #     super().__init__(name, age,food)
  #  def talk(self):
 #       return "Blub"
#class Cow(Animals):
    #def __init__(self,name,age,food):
   #     super().__init__(name, age,food)
  #  def talk(self):
 #       return "Muuu"
#When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)
#cat1 = Cat("Suzie", 12 , ["fish", "cake"])
#fish1 = Fish("Bob", 6 , ["pellets", "water"])
#cow1 = Cow("Mercy", 6 ,["grass", "water"])
#objects = [cat1, fish1, cow1]
#for i in objects:
 #   print(i.talk())

#2.The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6
#def snail(depth) -> int:
 #   tot = int(depth / 5)
  #  return (tot)
#print(snail(31))

#3.Write a function that takes a list of numbers and returns the largest number in the list
#def big(arr) -> int:
#    largest_number = arr[0]
 #   for number in arr:
    #    if number > largest_number:
       #     largest_number = number
 #   return largest_number
#test = [1000, 100, 10, 200, -1, 1000]
#print(big(test))

#4.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
#def count(x):
 #   big = 0
  #  small = 0
   # for i in x:
    #    if i.islower():
     #       small += 1
      #  elif i.isupper():
       #     big += 1
        #else:
         #   continue
    #return(f"LOWER CASE {small} \nUPPER CASE {big} ")
#print(count("Hello world!"))

#5.Using Object Oriented Programming, write a program that implements a dice game. The game should have two players, and each player should have a name and a score. The game should have a method called play that takes two players as arguments and simulates the game. The game should be played as follows:
#Each player rolls a die.
#The player with the highest roll wins the round.
#The winner gets one point added to their score.
#The game ends when one player has 5 points.
#The player with the most points at the end of the game wins.
#The program should print out the winner's name and score.
#If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.
import random
class Game:
    def __init__(self, player1 , player2):
        self.player1 = player1
        self.player2 = player2
    
    def play(self,player1, player2):
        players = [self.player1, self.player2]
        for player in players:
            i = 1
            while True:
                x= random.randint(1,6)
                print(x)
                if i <= 2 and x == 6:
                    x = random.randint(1,6)
                    i += 1
                    print(x)
                    players[player][1] = x
                else:
                    break
        if players[0][1]  > players[1][1]:
            players[0][1] += 1
        else:
            players[1][1] += 1
        if (players[0][1] >= 5) or (players[1][1] >= 5):
            if players[0][1] > players[1][1]:
                return f"Winner is {players[0][0]} with {players[0][1]} points."
            else:
                return f"Winner is {players[1][0]} with {players[1][1]} points."

one = ["Arthur", 0]
two = ["Ceasor", 0]
obj = Game( ["Arthur", 0], ["Ceasor", 0])
print(obj.play( ["Arthur", 0], ["Ceasor", 0]))
   
#6.Write a Python program that lists out all the default as well as custom properties of the class.
#class Show:
 #   def __init__(self, property1, property2, porperty3):
  #      self.property1 = "right"
   #     self.property2 = "down"
    #    self._property3 = "up"
    #def show(self):
     #   return f"Properties: \n{self.property1} \n{self.property2} \n{self._property3}"
#obj = Show("right", "down", "up")
#print(obj.show())

#7.Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.
#class Stack:
 #   def __init__(self, item, lst, length):
  #      self.item = item
   #     self.length = length    

    #def pop(self):
     #   if len(self.lst) != 0:
      #     self.lst.pop(-1)
       #    return self.lst
        #else:
         #   return 'The list is already empty'

    #def size(self):
     #   return len(self.lst)

    #def push(self,item):
     #   if len(self.lst) < self.length:
      #      self.lst.insert(0,self.item)
       #     return self.lst
        #else:
         #   return "list is full"

#8.Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.
#def square(arr):
 #   arr = [x**2 for x in arr]
  #  return(arr)
#axe = [1,2,3,4,5,6]
#print(square(axe))
#9.Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).
#class Queue:
 #   def __init__(self, element, lst, size):
  #      self.element = element
   #     self.lst = lst
    #    self.size = size
    #def dequeue(self):
     #   if len(self.lst) != 0:
      #      self.lst.pop()
       #     return self.lst
        #else:
         #   return 'The list is already empty'

    #def length(self):
     #   return len(self.lst)

    #def enqueue(self,element):
     #   if len(self.lst) < self.size:
      #      self.lst.insert(0,self.element)
       #     return self.lst
        #else:
         #   return "list is full"

#10.Using a while loop, implement merge sort algorithm.
#def mergeSort(array):
 #   if len(array) > 1:
  #      r = len(array)//2
   #     L = array[:r]
    #    M = array[r:]
     #   mergeSort(L)
      #  mergeSort(M)

       # i = j = k = 0
        #while i < len(L) and j < len(M):
         #   if L[i] < M[j]:
          #      array[k] = L[i]
           #     i += 1
            #else:
             #   array[k] = M[j]
              #  j += 1
            #k += 1
        #while i < len(L):
         #   array[k] = L[i]
          #  i += 1
           # k += 1

        #while j < len(M):
         #   array[k] = M[j]
          #  j += 1
           # k += 1
#def printList(array):
 #   for i in range(len(array)):
  #      print(array[i], end=" ")
   # print()
##   array = [60, 15, 2, 100, 99, -1]
    #mergeSort(array)

    #print("Sorted array is: ")
    #printList(array)



