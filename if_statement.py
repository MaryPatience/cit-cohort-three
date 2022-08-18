from operator import truediv


#is_coke=False
#is_fanta=False
#is_mirinda=False
#if is_fanta:
 #   print("Buy fanta")
#elif is_coke:
 #   print("Buy coke")
#elif is_mirinda:
 #   print("Buy mirinda")
#else:
 #   print("Buy water")      

temp=int(input("Enter temperature:"))
print("Which conversion do you want to do?")
print("A:   Celcius to Fahrenheight")
print("B:   Fahrenheight to Celcius")
choice=input()

if choice=="A":
    print(str((temp*9.0/5.0)+32)+"°F")# formular for changing from celcius to fahrenheight appended to the units.
elif choice=="B":
    print(str((temp-32)*5.0/9.0)+"°C")# formular for changing from fahrenheight to celcius appended to the units. 
else:
    print("Please enter choice!")
    