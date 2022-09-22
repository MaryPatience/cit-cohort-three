#1.Create a 2-D array and slice out the second number in the second column
arr = [[1,2,3],[3,4,3],[5,6,3],[7,8,3],[8,9,3]]
print(arr[1][1])
#2.Write a python program to sort array element in the ascending/descending order
arr=[12,1,2,3,4,56,78,9,8]
print ("The array: "+str(arr))
print ("The array sorted in ascending order: "+str(sorted(arr)))
arr.sort(reverse=True)
print("The array sorted in descending order: "+str(arr))
#3.Write a python program to find the maximum and minimum value in a given 2-D array
from numpy import amax
from numpy import amin
from numpy import array
arr = array([[1,2,3],[3,4,3],[5,6,3],[7,8,3],[8,19,3]])
M = amax(arr)
N = amin(arr)
print("Maximum = "+str(M))
print("Minimum = "+str(N))
#4.Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
#percentage less than 50 (Grade C)
#percentage equal to 50 and less than 80 (Grade B)
#percentage equal to 80 and more than 80 (Grade A)
print("My grading program")
grades = [0,0,0,0,0]
sum=0
for i in range(len(grades)):
    grades[i]=int(input("Enter Grade "+str(i+1)+" :"))
    sum+=grades[i]
print("Total = "+str(sum))
ave = float(sum)/5
print("Average percentage = "+str(ave))
if ave<50:
    print("Grade C")
elif ave==50 and ave<80:
    print("Grade B")
else:
    print("Grade A")
#5.Write a python program to fetch only Email ID from text file which include following fields -:
#Name
#Mobile Number
#Roll Number
#Email ID
def email(txt_file):
    the_email=None
    f=open(txt_file, "r")
    for line in f.readlines():
        if '@'in line:
            the_email=line.strip()
    return the_email
print(email("txt_file.txt"))
#6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
#If speed is less than 70, it should print “Ok”.
#Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#If the driver gets more than 12 points, the function should print: “License suspended”
def traf(speed):
    if speed<70:
        print("OK")
        D=0
    else:
        km=int(input("How many kilometers: ")) #kilometers traveled at high speed
        if km>5:
            D=km/5  #demerit points initialised
            print("Points :"+str(D))
            if D>12:
                print("License suspended")
            else:
                D=km/5
        else:
            D=0
            print("Points :"+str(D))
    return D
print(traf (75))
#7.Write a function called show_stars(rows).
def stars(rows):
     ls=' '
     for i in range(rows):
        ls+='*'
        print(ls)
print(stars(4))  
# 8.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3000):
    if i%7==0 and i%5!=0:
        print(str(i),end=",")  
#9.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
abc=input("Enter a sequence of values separated  by commas: ")
def organise(abc):
    split=list(abc.split(","))
    cut=tuple(abc.split(","))
    print (split)
    print(cut)
    return 
print(organise(abc))
#10.Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.
from math import sqrt
C=50
H=30
sam="100,150,180"
ab=list(sam.split(","))
print(ab)
for i in range(len(ab)):
    D=int(ab[i])
    Q = sqrt(((2 * C * D)/H))
    print(int(Q),end=",")
#11.Write a function to compute 5/0 and use try/except to catch the exceptions.
def five(m):
    try:
        print(m/0)
    except:
        print("Something went wrong!")
print(five(5))
#12.Create a nesting list that prints out the color and the car brand.    
nest=[['1:','Red','Benz'],['2:','Pink','Jeep'],['3:','Blue','Aston Martin'],['4','Black','BMW']]
print(nest)
choice=int(input('Enter car choice: '))
z=choice-1
fav=' '.join(nest[z])
print(fav)

#13.Bonus Question: Algorithm challenge: Create your own sorting algorithm.
# An algorithm is a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.
# For sorting, we shall assume that our program is working with an array.
#Sorting can be done either in descending or ascending order. Therefore, we specify which kind of order we want the sorted array elements to be arranged.
#Sorting can also be done based on several different parameters like alphabetical order, position of integer on the number line, length of elements and so on.
#Upon the user specifying the kind of sorting he/she wants, the array elements are organised in the user's desired order.


