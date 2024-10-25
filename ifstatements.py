marks=70
if marks>=50 and marks<=100:
    print("pass")
else:
    print("failure")

num=20
if num%2==0:
    print("even")

else:
    print("odd")

# num1=int(input("enter number: "))
# num2=int(input("enter number: "))
# num3=int(input("enter number: "))

# if num1>num2 and num1>num3:
#     print("num1 is greater")

# elif num2>num1 and num2>num3:
#     print("num2 is greater")
 
# else:
#     print("num 3 is greater")


# temp=int(input("enter temp: "))

# if temp>=30:
#     print("the temp is too high")

# elif temp>=15 and temp<=30:
#     print("normal temp")

# else:
#     print("cold temp")


# x=int(input("enter number: "))
# y=int(input("enter number: "))
# if x>=10 and x<=20 and y>=100:
#  print("conditon met")
# else:
#  print("condition not met")


# marks=int(input("enter marks: "))
# if marks>=90 and marks<=100:
#   print("A")
# elif marks>=80 and marks<=90:
#   print("B")
# elif marks>=70 and marks<=80:
#   print("C")
# elif marks>=60 and marks<=70:
#   print("D")
# elif marks>=50 and marks<=60:
#   print("E")
# else:
#     print("fail")

# age=int(input("enter age: "))  
# if age>=60:
#   print("older")
# elif age>18 and age<=60:
#   print("adult")
# else:
#    print("minor")

# #nested if statements
# purchase=int(input("Enter amount: "))
# if purchase>=1000:
#   print("100sh discount")
#   if purchase>=5000:
#     print("200sh discount")
# else:
#       print("no discount")

# age1=int(input("enter your age: "))
# if age1>=18:
#   licenses=input("do you have a license yes/no: ").lower().strip()
#   if licenses=="yes":
#     print("eligible to drive")
#   else:
#     print("you are not eligible to drive")
# else:
#   print("you are to young to drive")


# # Write a program that:
# # =>Takes the user's credit score and annual income as input.
# # =>If the credit score is above 700, check if the income is above $50,000:
# # =>If both conditions are met, print "Loan approved."
# # =>If only the credit score is high, print "Income requirement not met."
# # =>If the credit score is below 700, print "Credit score too low."


credit_score=int(input("Enter credit score: "))
annual_income=float(input("Enter annual income: "))

# if credit_score>700 and annual_income>=50000:
#   print("loan approaved")
#   if credit_score>700 and annual_income<50000:
#     print("income required not met")
# else:
#   print("credit score too low")
  
if credit_score>700:
  if annual_income>50000:
    print("loan approved")
  else:
     print("income required not met")
else:
 print("credit score too low")





 