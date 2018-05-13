'''
Alec McDaugale
This is a deck of cards. The plan is to eventually use this to make a gui card game. This is basic concept at this time.
'''
class Cards:
    def __init__(self):
        self._deck = Deck


class Deck:
    def __init__(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self._deck = [suit, cards, values]

    def get_deck(self):
        return  self._deck

    def to_string(self):
        for val in self._deck:
            print(val)


deck = Deck()
deck.to_string()