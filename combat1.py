import random

def roll20():
    roll = int(random.randrange(1, 20, 1))
    return roll
def roll8():
    roll = int(random.randrange(1, 8, 1))   
    return roll

playerhp = 15
trollhp = 12
print("a troll approaches!")
while True:
    playerRoll = roll20()
    if playerRoll >= 8:
        print("You hit with a roll of ", playerRoll)
        damageRoll = roll8()
        print("you roll ", damageRoll, "for damage")
        input("...")
        trollhp -= damageRoll
    else:
        print("you miss with a roll of ", playerRoll)
        input("...")
    trollRoll = roll20()
    if trollRoll >= 10:
        print("the troll hits with a roll of ", trollRoll)
        damageRoll = roll8()
        print("the troll rolls ", damageRoll, "for damage")
        input("...")
        playerhp -= damageRoll
    else:
        print("The troll misses with a roll of", trollRoll)
        input("...")
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
        
        
        
    


