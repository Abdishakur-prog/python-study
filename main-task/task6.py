# ASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.


attempts=4
correct_password="admin@123"

# for i in range(attempts):
#     password=input(" Enter your password: ")
#     if password==correct_password:
#         print("Access granted")
#         break
#     else:
#         print("Access denied")

# else:
#     print("Account blocked due too many attempts")


for i in range(attempts):
    password=input(" Enter your password: ")
    remaining_attempts=attempts-(i+1)
    if password==correct_password:
        print("Access granted")
        break      
    else:
        remaining_attempts=attempts-(i+1)
        print(f"incorrect password you have {remaining_attempts} attempts remaining")
        if remaining_attempts==0:
            display="Account blocked"
print(display)