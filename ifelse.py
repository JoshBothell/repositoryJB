
##age = input("what is your age? ")
##
##if age < "65" or age > "16" and age.isdigit():
##    print("I can drive")
##elif age > 65 and age.isdigit():
##    print("Sorry! you can't drive you can't see")
##elif age < 16 and age.isdigit():
##    print("You need to grow up")
##else:
##    print("you shouldnt be driving")

num1 = input("enter a number ")
num2 = input("enter a number ")

if num1.isdigit() and num2.isdigit():
    print(num1,num2, "are both digits")
elif num1.isdigit() or num2.isdigit():
    print("only one of the numbers is a digit.")
else:
    print("Those are not digits.")
           
