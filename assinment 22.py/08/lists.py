#1. Write a Python program to sum all the items in a list.
 #   - The list should be generated using list comprehension
  #  - The size of the list should be from a user input
n=int(input("Enter number of list components:"))
abd = [int(input()) for x in range(n) ]
print (abd)
x=sum(abd)
print(x)
#2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`
abd = []
n=int(input("How many string list components? "))
abd = [input() for x in range(n) ]
print(abd)
abd=[y for y in abd if (len(y)>1) and (y[0]==y[-1])]
print(len(abd))
#3. Write a Python program to remove duplicates from a list, given list
    #`fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`
fruits =["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
print(fruits)
results=[]
[results.append(i) for i in fruits if i not in results]
print(results)
#4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`
Sample_List = ['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
del Sample_List[5] 
del Sample_List[4] 
del Sample_List[0]
print(Sample_List)
#5. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
val=[]
i=1
while i<=30:
    val.append(i**2)
    i+=1
del val[0:5]
print(val)
    

