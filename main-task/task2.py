# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
num=int(input("Enter Number: "))

if num%2==0:
    print("Number is even")
else:
    print("Number is odd")