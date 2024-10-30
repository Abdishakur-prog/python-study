# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32) ]
# Display the total quantity of the 3 above.

#Q1
x=list(range(1,51))
print(x)

#Q2
x=range(1,51)
for num in x:
    if num%7==0 or num%5==0:
        print(num)


#Q3
sum=0
num=(range(10,41))
for x in num:
  sum=sum+x
print(sum)
average=sum/len(num)
print(average)
 
# 
# # for x in range(10,50):
# #     if x%2!=0 or x%2!=0:
# #       print(x)
# #     

count=0
num2=range(10,41)
odd_numbers=[]

for x in num:
   if x%2!=0:
      odd_numbers.append(x)
      if count==10:
        break
print(count)

    
numbers=int(input("enter number: "))

for i in range(11):
   mult=numbers*i
   print(f'{numbers}*{i}={mult}')


value=range(1,51)
for x in value:
    if x %2==0:
        print(x)

total_quantity=0
ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32) ]

for i in ls1:
    stock=i[1]
    total_quantity+=stock
    print(total_quantity)


