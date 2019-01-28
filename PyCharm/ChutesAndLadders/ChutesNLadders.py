# Chutes and Ladders
# JoshBothell
# 1/19

import random

EMPTY = " "
p1p = []
for i in range(0, 100):
    p1p.append(EMPTY)
p2p = []
for i in range(0, 100):
    p2p.append(EMPTY)
p3p = []
for i in range(0, 100):
    p3p.append(EMPTY)
p4p = []
for i in range(0, 100):
    p4p.append(EMPTY)


class Player (object):
    def __str__(self):
        strx = self.name + " is player number " + str(self.player_num)
        return strx

    def __init__(self, name, num):
        self.name = name
        self.player_num = num
        self.position = -1
        self.piece = self.name[0]

    def roll(self):
        roll = random.randint(1, 6)
        print("you rolled a", roll)
        return roll

    def move(self):
        move_roll = self.roll()
        if self.position + move_roll <= 99:
            old_pos = self.position
            self.position = self.position + move_roll
            if self.player_num == 1:
                p1p[old_pos] = EMPTY
                p1p[self.position] = self.piece
            elif self.player_num == 2:
                p2p[old_pos] = EMPTY
                p2p[self.position] = self.piece
            elif self.player_num == 3:
                p3p[old_pos] = EMPTY
                p3p[self.position] = self.piece
            elif self.player_num == 4:
                p4p[old_pos] = EMPTY
                p4p[self.position] = self.piece

    def win(self):
        if self.position == 99:
            return self.piece
        else:
            return None


class Board(object):
    pass


class Space(object):
    pass


def ask_num():
    pass


def switch_turn():
    pass


def winner_congrats():
    pass


def main():
    player1 = Player("Josh", 1)
    print(player1)
    while p1p[99] == EMPTY:
        player1.move()
        winner = player1.win()
        print(player1.position)
        print(winner)



main()
