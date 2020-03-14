class Hand:

    def __init__(self):
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards += [card]
        self.score += card.value


class BlackJackHand(Hand):

    def __init__(self):
        super().__init__()
        self.aces = 0
        self.result = ''
        self.blackjack = False
        self.bust = False

    def add_card(self, card):
        self.cards += [card]
        self.score += card.value
        if card.rank == 'A':
            self.aces += 1

    def adjust_ace(self):
        while self.score > 21 and self.aces:
            self.score -= 10
            self.aces -= 1
