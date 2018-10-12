import random
import time
def roll(dice):
    dice = dice
    dice += 1
    roll = int(random.randrange(1, dice))
    return roll

while True:
    x = roll(20)
    print(x)
    time.sleep(0.05)
        
