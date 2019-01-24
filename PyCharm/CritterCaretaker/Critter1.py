# Josh Bothell
# 1/19
# Tamagotchi Proto
import random
import keyboard
import time


class Critter(object):
    def __str__(self):
        return "This is a critter named", self.name

    def __init__(self, name):
        self.name = name
        self.__hunger = random.randint(0, 11)
        self.__boredom = random.randint(0, 16)
        print(self.name, "has been born!")

    def pass_time(self):
        self.__hunger += random.randint(0, 3)
        self.__boredom += random.randint(0, 3)

    def play(self):
        print("You play with", self.name)
        fun = random.randint(0, 11)
        print(self.name, "has its boredom reduced by", fun)
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        print(self.name + "'s new boredom level is" + str(self.__boredom))

    def check_up(self):
        print(self.name, "is", self.mood)
        print(self.name, "has a boredom level of", self.__boredom, "\ntheir hunger is at", self.__hunger)

    def feed(self):
        print("You feed", self.name)
        food = random.randint(0, 11)
        print("His hunger is reduced by", food)
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        print("His hunger is now", self.__hunger)

    @property
    def mood(self):
        unhappiness = (self.__hunger + self.__boredom) / 2
        if unhappiness < 15:
            mood = "Happy"
        elif unhappiness < 30:
            mood = "Okay"
        elif unhappiness < 45:
            mood = "Unhappy"
        else:
            mood = "Upset!"
        return mood


critter = Critter("Chungo")
time_passed = 0
while True:
    if keyboard.is_pressed('H'):
        print("""
Critter commands can be entered at any time, they are as follows:

        C - Check up on your critter
        
        F - Feed your critter
        
        P - Play with your critter
        
        """)
        input("Press Enter to continue  ")
    elif keyboard.is_pressed('C'):
        critter.check_up()
        input("Press Enter to continue  ")
    elif keyboard.is_pressed('F'):
        critter.feed()
        input("Press Enter to continue  ")
    elif keyboard.is_pressed('P'):
        critter.play()
        input("Press Enter to continue  ")
    else:
        time_passed += 1
        if time_passed == 50000:
            critter.pass_time()
            print("Time has passed")
            print(critter.name, "is", critter.mood)
            print("press h to view critter commands\n...")
            time_passed = 0
            continue
        else:
            continue
