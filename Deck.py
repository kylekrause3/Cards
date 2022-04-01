from Card import *
from Suit import *


class Deck:
    RANKS = Card.RANKS  # list
    UNICODE_SUITS = Card.UNICODE_SUITS  # list
    SUITS = Card.SUITS  # dictionary

    def __init__(self, *isEmpty: bool):
        self.cards = []

        if len(isEmpty) > 1:
            raise ArgumentAmountError("Too many arugments given to Deck class")
        elif len(isEmpty) == 0:
            for i in range(len(Card.SUITS)):
                for j in range(len(Card.RANKS)):
                    self.cards.append(Card(i + 1, j+ 1, False))
        elif isinstance(isEmpty[0], bool):
            if isEmpty[0]:
                pass
            else:
                for i in range(len(Card.SUITS)):
                    for j in range(len(Card.RANKS)):
                        print(str(i))
                        self.cards.append(Card(i + 1, j + 1, False))

    def __str__(self):
        ret = ''
        for i in self.cards:
            ret += f"{i}\n"
        return ret

    def shuffle(self):
        for i in range(len(self.cards)):
            self.swapCards(i, random.randint(1, len(self.cards) - 1))

    def swapCards(self, x, y):
        cache = self.cards[x]
        self.cards[x] = self.cards[y]
        self.cards[y] = cache

    def getCard(self, x : int):
        if x > len(self.cards) or x < len(self.cards):
            raise CardOutOfRangeError(f"Card index out of range: {x}")
        return self.cards[x]


class CardOutOfRangeError(Exception):
    pass

