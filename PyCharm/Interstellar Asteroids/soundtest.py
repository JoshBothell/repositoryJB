# sound and music

from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

# load fx
shoot = games.load_sound("Sounds/Shoot.wav")
thrust = games.load_sound("Sounds/Thrust.wav")
explosion = games.load_sound("Sounds/Asteroid Explosion.wav")
levelup = games.load_sound("Sounds/Level Up.wav")

# load theme
games.music.load("Sounds/Interstellar.wav")

# create menu
choice = None
while choice != "0":
    print(
        """
        Sound and Music
        
        0 - Quit
        1 - Play shoot sound
        2 - Loop Thrust sound
        3 - Stop Thrust sound
        4 - Play Theme
        5 - Loop Theme
        6 - Stop Theme
        7 - Play Level Up sound
        8 - Play Explosion sound
        """
    )
    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Goodbye!")
    elif choice == "1":
        shoot.play()
        print("Playing shoot sound")
    elif choice == "2":
        loop = int(input("How many additional times? (-1 = forever)  "))
        thrust.play(loop)
    elif choice == "3":
        thrust.stop()
        print("stopped")
    elif choice == "4":
        games.music.play()
    elif choice == "5":
        loop = int(input("How many additional times? (-1 = forever)  "))
        games.music.play(loop)
    elif choice == "6":
        games.music.stop()
    elif choice == "7":
        levelup.play()
        print("Playing level up sound")
    elif choice == "8":
        explosion.play()
        print("Playing explosion sound")

