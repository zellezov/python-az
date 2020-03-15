class Balance:

    def __init__(self):
        self.total = 100.0
        self.bet = 0

    def bet_won(self, payout):
        if payout > 0:
            print('You win ' + str(int(payout)))
        self.total += payout

    def bet_lost(self):
        self.total -= self.bet


class BaccaratBalance(Balance):

    def __init__(self):
        super().__init__()
        self.player_bet = 0
        self.tie_bet = 0
        self.banker_bet = 0

    def flush_bets(self):
        self.player_bet = 0
        self.tie_bet = 0
        self.banker_bet = 0


class Payout:

    def __init__(self, balance):
        self.balance = balance


class BlackjackPayout(Payout):

    def __init__(self, balance):
        super().__init__(balance)

    def straight(self):
        return self.balance.bet

    def blackjack(self):
        return self.balance.bet * 1.5


class BaccaratPayout(Payout):

    def __init__(self, balance):
        super().__init__(balance)

    def player(self):
        return self.balance.player_bet + self.balance.player_bet

    def tie(self):
        return self.balance.tie_bet * 8 + self.balance.tie_bet

    def banker(self):
        return self.balance.banker_bet * 0.95 + self.balance.banker_bet
