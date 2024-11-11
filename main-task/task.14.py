# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

# value=input("Enter first number")
# value2=input("Enter second number")

while True:
    try:
      input1=float(input("Enter first number: "))
      input2=float(input("Enter first number: "))

      results=input1+input2
      print(results)
      break

    except:
       print("invalid character")






