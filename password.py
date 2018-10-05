#JoshBothell
#10/1/18
#password program

def check_account(username, password):
    x = 0
    while x == 0:
        username = username
        password = password
        enterusername = input("USERNAME: ")
        enterpassword = input("PASSWORD: ")
        if username == enterusername and password == enterpassword:
            print("ACCESS GRANTED")
            x = 1
            return True
        else:
            print("ACCESS DENIED")
def get_password():
    print("your password must start with a capital letter \n and must contain at leat 1 symbol \n and must be at least 10 characters long")
    password = input("enter your password ")
    if password.istitle() and  not password.isalnum() and len(password) >= 10:
        print("Your password is set!")
        return password
    else:
        print("Your password didn't meet the requirements")
        get_password()
def get_username():
    print("username should only contain numbers and letters\ncan only contain 20 characters\n must be more than 1 character.")
    username = input("... ")
    if username.isalnum() and len(username) >= 3 and len(username) <= 20:
        print("Your username is set!")
        return username
    else:
        print("Your username didn't meet the requirements")
        get_username()
def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("... "))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            print(username, password)
            choice = 0
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login
def main():
    password, user_name, access = menu()
    if access == True:
        print("you got in")
    else:
        print("thats not right")


main()
