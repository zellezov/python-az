import random


class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '[' + self.rank + self.suit + ']'


class Deck:

    def __init__(self):
        # hearts, diamonds, spades, clubs
        self.suits = (u'\u2665', u'\u2666', u'\u2660', u'\u2663')
        self.ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                       'K': 13, 'A': 14}
        self.deck = []

    def __str__(self):
        print(self.deck)

    def build(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck += [Card(suit, rank, self.values[rank])]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop(0)
        return dealt_card

    def print_deck(self):
        for k, v in self.values.items():
            print('\n' + k, v)


class BlackJackDeck(Deck):

    def __init__(self, values=None):
        super().__init__()
        if values is None:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                      'K': 10, 'A': 11}
        self.values = values


class BaccaratDeck(Deck):

    def __init__(self, values=None):
        super().__init__()
        if values is None:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0, 'J': 0, 'Q': 0, 'K': 0,
                      'A': 1}
        self.values = values
