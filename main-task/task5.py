# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1=int(input("Enter Number: "))
num2=int(input("Enter Number: "))
num3=int(input("Enter number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater")

elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
 
else:
    print(f"{num3}is greater")



