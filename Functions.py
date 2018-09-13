#Josh Bothell
#9/18
#get name function
def get_name():
#ask user for input
    name=input("what is your name: ")
#display name
    print("the name you entered was", name)

print("This is our function: ")
get_name()



def areaOfCircle():
    PI = 3.14159265
#1 get a radius
    radius = input("What is the radius of the circle: ")
    radius = float(radius)
#2  compute the area
    area= radius*radius*PI
#3 display infor
    print("the area of the circle is", area)

areaOfCircle()
