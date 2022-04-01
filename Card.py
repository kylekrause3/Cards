class Card:
    RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    UNICODE_SUITS = [u'\u2663', u'\u2666', u'\u2665', u'\u2660'] # [♣,♦,♥,♠]  Clubs, Diamonds, Hearts, Spades
    SUITS = {
        1:'clubs',
        2:'diamonds',
        3:'hearts',
        4:'spades'
    }

    '''suit : int. num : int, dealt : bool'''
    def __init__(self, suit, num: int, *flippedOver : bool): # suit will be int
        # makes sure suit is integer
        if isinstance(suit, str):
            self.suit = self.suitStrAsInt(suit )
        elif isinstance(suit, int):
            self.suit = suit - 1
        else:
            raise SuitError("Suit provided", suit, "is not an eligble suit")

        # makes sure that 1 <= number <= 13
        if num > len(self.RANKS):
            print('number provided is outisde of range, bringing down to card number')
            while num > len(self.RANKS):
                num -= 13
        if num <= 0:
            print('number provided is outisde of range, bringing down to card number')
            while num <= 0:
                num += 13
        self.num = num

        # if no arg is provided, makes dealt False, elif makes this provided value
        if len(flippedOver) > 1:
            raise ArgumentAmountError("Too many arguments provided to Card class")
        elif flippedOver[0]:
            self.flippedOver = True
        else:
            self.flippedOver = False

    def flip(self):
        self.flippedOver = not self.flippedOver

    def isFlipped(self):
        return self.flippedOver

    def getSuit(self):
        return self.suit

    def suitStrAsInt(self, suitStr):
        return list(self.SUITS.values()).index(suitStr)

    def suitIntAsStr(self):
        return self.SUITS[self.suit + 1]

    def __str__(self):
        return f"{self.RANKS[self.num - 1]} of {self.suitIntAsStr()} ({self.num}{self.UNICODE_SUITS[self.suit]}), Flipped: {self.flippedOver}"


class SuitError(Exception):
    """Raised when Suit provided is incompatible with class"""
    pass


class ArgumentAmountError(Exception):
    """Raised when Card Class is given more arguments than expected"""
    pass

