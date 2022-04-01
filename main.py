from Card import *
from Deck import *


if __name__ == '__main__':
    x = Deck()
    print(x)
    x.getCard(52).flip()
    print(x.getCard(2), "\n", x)

