'''
Alec McDaugale
This is a deck of cards. Begining to create a blackJack class. Displays two cards and the value.
'''
import random


class BlackJack:
    def __init__(self):
        self._deck = Deck()
        self._cards = []
        self._cardsvalue = []
        #self._total
        self._dealercards = []
        self._dealercardsvalue = []
        #self._dealertotal
        #self.deal_cards(2)

    def deal_card(self, cardset, value):
        num = random.randint(0, 12)
        cardset.append(self._deck.get_cards(num))
        value.append(self._deck.get_values(num))
        #total += int(value[len(value)-1])

    def deal_cards(self, num):
        for index in range(num):
            self.deal_card(self._cards, self._cardsvalue)
            self.deal_card(self._dealercards, self._dealercardsvalue)

    def get_cards(self):
        return self._cards

    def get_dealer_cards(self):
        return self._dealercards

    def get_total(self, value):
        total = 0
        for val in value:
            total += val
        return total


    '''def get_total(self):
        return self._total
    def get_dealer_total(self):
        return self._dealertotal'''

    def to_string(self):
        print("Dealer")
        print("Total:", self.get_total(self._dealercardsvalue))
        for val in range(len(self._dealercards)):
            print(self._dealercards[val], end=" ")
        print("\n")
        for val in range(len(self._cards)):
            print(self._cards[val], end=" ")
        print("\nTotal:", self.get_total(self._cardsvalue))
        print("Player")


class Deck:
    def __init__(self):
        self._values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self._cards = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self._suit = ("Hearts", "Diamonds", "Spades", "Clubs")
        self._deck = (self._suit, self._cards, self._values)

    def get_deck(self):
        return  self._deck

    def get_values(self, index):
        return self._values[index]

    def get_cards(self, index):
        return self._cards[index]

    def get_suit(self, index):
        return self._suit[index]

    def to_string(self):
        for index1 in range(4):
            for index2 in range(13):
                print(self._suit[index1], self._cards[index2])


#deck = Deck()
#deck.to_string()
game = BlackJack()
game.deal_cards(2)

game.to_string()

