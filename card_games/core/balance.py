class Balance:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def bet_won(self, payout):
        print('You win ' + str(payout))
        self.total += payout

    def bet_lost(self):
        self.total -= self.bet


class Payout:

    def __init__(self, bet):
        self.bet = bet


class BlackjackPayout(Payout):

    def __init__(self, bet):
        super().__init__(bet)

    def straight(self):
        return self.bet

    def blackjack(self):
        return self.bet * 1.5
