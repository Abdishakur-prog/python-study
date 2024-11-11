#Function to calculate the area of triangle;

def area_triangle():
    base=90
    height=40
    area=base*height*0.5
    return area
m=area_triangle()
print(m)

def area_rectangle(length,width):
    area=length*width
    return area
y=area_rectangle(40,90)
print(y)

def triangle(base,height):
    area=base*height*0.5
    return area
x=triangle(60,70)
print(x)



def num():
    number=int(input("Enter number: "))
    if number%2==0:
        return ("even")
    else:
        return ("odd")
z=num()
print(z)    


def largest_num(num1,num2,num3,num4):
    if num1>num2 and num1>num3:
        return f"{num1} is greater"
    elif num2>num1 and num2>num3:
        return f"{num2} is greater"
    elif num3>num1 and num3>num2:
        return f"{num3} is greater"
    else:
        return f"{num4} is greater"


num1=(int(input("Enter Number: ")))
num2=(int(input("Enter Number: ")))
num3=(int(input("Enter Number: ")))
num4=(int(input("Enter Number: ")))

o=largest_num(num1,num2,num3,num4)

print(o)






    