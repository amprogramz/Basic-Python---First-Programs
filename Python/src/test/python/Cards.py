'''
Alec McDaugale
This is a deck of cards. The plan is to eventually use this to make a gui card game. This is only a basic concept at
this time.
'''
class Cards:
    def __init__(self):
        self._deck = Deck


class Deck:
    def __init__(self):
        self._values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
        self._cards = ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self._suit = ("Hearts", "Diamonds", "Spades", "Clubs")
        self._deck = (self._suit, self._cards, self._values)

    def get_deck(self):
        return  self._deck

    def to_string(self):
        for index1 in range(4):
            for index2 in range(14):
                print(self._suit[index1], self._cards[index2])


deck = Deck()
deck.to_string()