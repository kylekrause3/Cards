'''
TODO: ADD ISEMPTY, ISFULL TO BE ABLE TO ADD CARDS TO SPECIFIC SUIT


UNUSED AS OF NOW
'''

import random

from Card import *


class Suit:
    RANKS = Card.RANKS  # list
    UNICODE_SUITS = Card.UNICODE_SUITS  # list
    SUITS = Card.SUITS  # dictionary

    def __init__(self, suit, *isEmpty: bool):
        self.cards = []

        if not isEmpty:
            # makes sure suit is integer
            if isinstance(suit, str):
                self.suit = Card.suitStrAsInt(suit)
            elif isinstance(suit, int):
                self.suit = suit
            else:
                raise SuitError("Suit provided", suit, "is not an eligble suit")
            for i in range(13):  # adds 13 cards, all flipped down, to the suit
                new_card = Card(suit, i)
                self.cards.append(new_card)
        else:
            # makes sure suit is integer
            if isinstance(suit, str):
                self.suit = Card.suitStrAsInt(suit)
            elif isinstance(suit, int):
                self.suit = suit
            else:
                raise SuitError("Suit provided", suit, "is not an eligble suit")

    def shuffle(self):
        for i in range(len(self.cards)):
            self.swapCards(i, random.randint(1, len(self.cards)))

    def swapCards(self, x, y):
        cache = self.cards[x]
        self.cards[x] = self.cards[y]
        self.cards[y] = cache


'''
function shuffleArr(){
  for(let i = 0; i < arr.length; i++){ //shuffles the array
    let r = parseInt(random(0, arr.length));
    swap(i, r);
  }
}

function swap(x, y){
  var cache = arr[x];
  arr[x] = arr[y];
  arr[y] = cache;
}
'''
