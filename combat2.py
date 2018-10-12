import random

def roll12():
    roll = int(random.randrange(1, 12, 1))
    return roll

playerhp = 250
trollhp = 225
print("a troll approaches!")
while True:
    pdamageRoll = roll12()
    print("you do ", pdamageRoll, "damage")
    input("...")
    trollhp -= pdamageRoll
    tdamageRoll = roll12()
    print("the troll does ", tdamageRoll, "damage")
    input("...")
    playerhp -= tdamageRoll
    if playerhp <= 0:
        print("YOU DIED")
        input("...")
        break
    elif trollhp <= 0:
        print("You defeated the troll!")
        input("...")
        break      
    print("Player HP: ", playerhp)
    print("Troll HP: ", trollhp)
    input("...")
        
        
        
