# Josh Bothell
# 2/19
# War
# Two players play war against each other.

######################################################################
# imports
import cards, games


######################################################################
# classes

class WarCard(cards.Card):
    """A card for the game war."""

    @property
    def value(self):
        if self.is_face_up:
            value = WarCard.RANKS.index(self.rank) + 1
            if value == 1:
                value = 14
                return value
            else:
                return value
        else:
            return None


class WarDeck(cards.Deck):
    """A War Deck"""

    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                card = WarCard(rank, suit, True)
                self.add(card)


class WarHand(cards.Hand):
    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(WarHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has a value of None, then total is none
        for card in self.cards:
            if not card.value:
                return None
        # add up card values.
        t = 0
        for card in self.cards:
            t += card.value
        return t


def battle(hand1, hand2, pot):
    temp_hand1 = WarHand(hand1.name)
    temp_hand2 = WarHand(hand2.name)
    hand1.give(hand1.cards[-1], temp_hand1)
    hand2.give(hand2.cards[-1], temp_hand2)
    print(temp_hand1)
    print(temp_hand2)
    if temp_hand1.total > temp_hand2.total:
        winner = "1"
    elif temp_hand2.total > temp_hand1.total:
        winner = "2"
    else:
        temp_hand1.give(temp_hand1[0], pot)
        temp_hand2.give(temp_hand2[0], pot)
        war(hand1, hand2, pot)
        print(temp_hand1)
        print(temp_hand2)
    return winner


def war(hand1, hand2, pot):
    for i in range(3):
        hand1.give(hand1[0], pot)
        for card in hand1:
            card.flip()
    for i in range(3):
        hand2.give(hand2[0], pot)
        for card in hand2:
            card.flip()
    battle(hand1, hand2, pot)


def reward_winner(winner, hand1, hand2, pot):
    if winner == "1":
        for card in pot.cards:
            hand1.cards.append(card)
            pot.cards.remove(card)
    if winner == "2":
        for card in pot.cards:
            hand2.cards.append(card)
            pot.cards.remove(card)


def main():
    pot = WarHand("Pot")
    first_deck = WarDeck()
    first_deck.populate()
    first_deck.shuffle()
    name1 = input("Enter your name: ")
    name2 = input("Enter your name: ")
    big_hand1 = WarHand(name1)
    big_hand2 = WarHand(name2)
    big_hands = list([])
    big_hands.append(big_hand1)
    big_hands.append(big_hand2)
    first_deck.deal(big_hands, 26)
    while big_hand1.total > 0 and big_hand2.total > 0:
        battle(big_hand1, big_hand2, pot)


main()