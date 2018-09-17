#Josh Bothell
#9/18
import math

#get name function
def get_name():
#ask user for input
    name=input("what is your name: ")
#display name
    print("the name you entered was", name)

print("This is our function: ")
get_name()



def areaOfCircle(radius1):
    PI = 3.14159265
#1 get a radius
    radius = radius1
    radius = float(radius)
#2  compute the area
    area= radius*radius*PI
#3 display infor
    print("the area of the circle is", area)

radiusx=input("what is the radius: ")
areaOfCircle(radiusx)

def pythagoras_theorem(ap, bp):
    #a^2+b^2=c^2
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)
    print("the third side is ", c)

ax=input("enter the length of the first leg: ")
bx=input("enter the length of the second leg: ")
pythagoras_theorem(ax, bx)

#add numbers
def add_numbers(numA, numB):
    num1 = float(numA)
    num2 = float(numB)
    num3 = num1 + num2
    return num3
iNum1= input("enter a number: ")
iNum2 = input("enter a second number: ")
num4 = add_numbers(iNum1, iNum2)
print("the sum of your numbers is", num4)

