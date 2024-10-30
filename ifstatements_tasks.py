# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."

#Q1
num1=int(input("enter number: "))
num2=int(input("enter number: "))
num3=int(input("enter number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater")

elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
 
else:
    print(f"{num3}is greater")

#Q2
temp=int(input("enter temp: "))

if temp>=30:
    print("the temp is too high")

elif temp>=15 and temp<=30:
    print("normal temp")

else:
    print("cold temp")

#Q3
x=int(input("enter number: "))
y=int(input("enter number: "))
if x>=10 and x<=20:
    if y>100:
      print("conditon met")
else:
 print("condition not met")


#Q4
password=input("enter password: ")
correct_password="secret123"
if password=="secret123":
    print("Access granted")
else:
    print("Access denied")

#Q5 
student_score=int(input("Enter score: "))
attendance=int(input("enter attendance: "))

if student_score>90:
    if attendance>80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
 print("improvement")


#Q6 
amount=float(input("Enter amount: "))
account_type=(input("Enter account type standard/permium: ")).lower().strip()

if account_type=="standard":
    if amount>500:
        print("Transaction exceeds the limit for Standard accounts")
    else:
        print("Transaction approved")
elif account_type=="premium":
    if amount>1000:
        print("Transaction exceeds the limit for Standard accounts")
    else:
        print("Transaction approved")
else:
    print("invalid account type")
