#JBothell
#10/3


#Defining functions for all operators.
def add(x, y):
    x = x
    y = y
    ans = x + y
    return ans

def sub(x, y):
    x = x
    y = y
    ans = x - y
    return ans

def multi(x, y):
    x = x
    y = y
    ans = x * y
    return ans

def divide(x, y):
    x = x
    y = y
    if y == 0:
        print("uh oh, don't divide by zero! ")
        ans = 0
    else:
        ans = x / y
    return ans

def mod(x, y):
    x = x
    y = y
    ans = x % y
    return ans

#input function that initially checks the numbers before outputting them.
def inputNumbers():
    x = input("Enter the first value: ")
    op = input("Enter one of the following operators (+, -, *, /, %): ")
    y = input("Enter the second value: ")
    if x.isdigit() and y.isdigit() == True:
        digits = True
    else:
        digits = False
    if "+" in op or "-" in op or "*" in op or "/" in op or "%" in op:
        supOp = True
    else:
        supOp = False
    if digits and supOp == True:
        check = True
        return x, op, y, check
    else:
        print("something isnt quite right, ")
        check = False
        return x, op, y, check

def arithmetic(x, y):
    x = x
    y = y
    if op == "+":
        ans = add(x, y)
        print(ans)
    elif op == "-":
        ans = sub(x, y)
        print(ans)
    elif op == "*":
        ans = multi(x, y)
        print(ans)
    elif op == "/":
        ans = divide(x, y)
        print(ans)
    elif op == "%":
        ans = mod(x, y)
        print(ans)
def secondCheck(x, y, op):
    x = x
    y = y
    op = op
    if x.isdigit() and y.isdigit() == True:
        digits = True
    else:
        digits = False
    if "+" in op or "-" in op or "*" in op or "/" in op or "%" in op:
        supOp = True
    else:
        supOp = False
    if digits and supOp == True:
        check2 = True
        print("the numbers passed the second check. ")
    else:
        check2 = False
        print("the numbers did not pass the second check. ")
    return check2

mainloop = True
while mainloop == True:
    loop = True
    while loop == True:
        x, op, y, check = inputNumbers()
        if check == True:
            loop = False
        else:
            print("try again.")
    check2 = secondCheck(x, y, op)
    if check2 == True:
        x = float(x)
        y = float(y)
        arithmetic(x, y)
    else:
        print("try again.")
            
