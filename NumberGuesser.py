import random
attempts = 5
rangex = 100
def menu():
    choice = input("Enter play, credits, quit, gamble, or advanced: ")
    if choice.lower() == "play":
        play()
    elif choice.lower() == "credits":
        creditsx() 
    elif choice.lower() == "quit":
        quitx()
    elif choice.lower() == "gamble":
        gamble()
    elif choice.lower() == "advanced":
        advanced()
    else:
        print("enter a valid option")
        menu()
def play():
    global rangex
    global attempts
    attempt = 0
    number = random.randint(1, rangex)
    print("Try to guess what number im thinking of. \nGo ahead, the number is between 1 -", rangex)
    print("You have", attempts,"attempts.")
    while attempt < attempts:
        guess = input("")
        if not guess.isdigit():
            print("Please enter a number")
            continue
        guess = int(guess)
        if guess == number:
            print("Yay! good job you guessed it")
            break
        elif guess < number:
            print("Oh no! you are too low, try again")
            attempt += 1
        elif guess > number:
            print("Oh no! you are too high, try again")
            attempt += 1
    if attempt >= attempts:
        print("Oh no! you ran out of attempts...")
def advanced():
    global rangex
    global attempts
    while True:
        rangex = input("Enter the desired range of the number to guess:\n")
        if not rangex.isdigit():
            print("Enter a digit.")
            continue
        else:
            rangex = int(rangex)
            break
    while True:
        attempts = input("Enter the number of attempts allowed: \n")
        if not attempts.isdigit():
            print("Enter a digit.")
            continue
        else:
            attempts = int(attempts)
            break
    print("Settings changed! The range is now", rangex, "and the number of attempts is", attempts)
    menu()
def creditsx():
    print("BY JOSH BOTHELL AND MATTHEW WALKER PREVENTED BY SUPERGROVER")
    menu()
def quitx():
    exit()
menu()
