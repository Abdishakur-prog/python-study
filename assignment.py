my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

# 1. Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” . 


my_ds[2]
print(my_ds[2])

my_ds[3][2]["currency"]
print(my_ds[3][2]["currency"])


print(my_ds[3][1])


amount=my_ds[3][2]["amount"]=90
print(amount)
print(my_ds)

number=str(my_ds[4])
number=number[::-1]
print(number)
number=int(number)
print(number)

# convert to a list
my_ds[5]=list(my_ds[5])
# change john to jane 
(my_ds[5][1])="jane"
my_ds[5]=tuple(my_ds[5])
print(my_ds)

x=int(input("enter number"))
y=int(input("enter number"))
if x>=10 and x<=20 and y>=100
 print("conditon met")
else:
 print("condition not met")


 