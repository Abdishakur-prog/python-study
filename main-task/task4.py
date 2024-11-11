# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email=input(("Enter email: "))

if email in '@' and email in '.':
    print("valid email")
else:
    print("invalid email")


#Another way of writing this code:

if email.index("@")>0 and emai.index("@")<emil.index('.'):
    print("valid email")
else:
    print("invalid email")