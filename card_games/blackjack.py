from card_games.core.balance import Balance, BlackjackPayout
from card_games.core.deck import BlackJackDeck
from card_games.core.hands import BlackJackHand


def play_blackjack():
    print("Welcome to Blackjack table!")
    print("Hit cards, to score 21, but don't bust.")
    print("Blackjack pays 3 to 2.")
    print('Dealer must draw to 16 and stand on 17.')

    # prepare deck
    deck = BlackJackDeck()
    deck.build()
    deck.shuffle()

    # prepare balance
    balance = Balance()

    print('\nDeck is shuffled and ready for game. Total balance: ' + str(balance.total))
    is_playing = True
    while is_playing:

        # place bet
        place_bet(balance)

        # prepare hands
        player = BlackJackHand()
        dealer = BlackJackHand()

        # deal first
        print('\nDealing first card')
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

        # deal second
        print('Dealing second card')
        player.add_card(deck.deal())
        player.adjust_ace()
        dealer.add_card(deck.deal())
        dealer.adjust_ace()

        # reveal players cards and first dealer card
        initial_score(player, dealer)

        player_decision(deck, player)
        dealer_decision(deck, dealer)
        game_result(player, dealer, balance)

        if balance.total < 1:
            print('Balance too low')
            is_playing = False
        elif len(deck.deck) < 10:
            print('Not enough cards to play next round')
            is_playing = False
        else:
            next_round = input("Would you like to play next round? (y/n) ").lower()
            if next_round == 'y':
                continue
            else:
                print('Thank you for playing!')
                is_playing = False


def place_bet(balance):
    while True:
        try:
            balance.bet = int(input("\nHow many chips would you like to bet? (1-100) "))
        except ValueError:
            print("Input value must be an integer")
        else:
            if balance.bet > balance.total:
                print('Sorry, your bet exceeds balance ' + str(balance.total))
            else:
                break


def initial_score(player, dealer):
    print("\nInitial score:")
    print('Player cards are: ' + get_cards(player) + '. Score: ' + str(player.score))
    dealer_card = dealer.cards[0]
    print('Dealer card is: ' + dealer_card.rank + dealer_card.suit + ", <hidden>. Score: " + str(dealer_card.value))


def get_cards(hand):
    return ', '.join(str(card.rank + card.suit) for card in hand.cards)


def player_decision(deck, player):
    if player.score == 21:
        print("Amazing Blackjack for player")
        player.blackjack = True
    else:
        decision = True
        while decision:
            if player.score < 21:
                hit_stand = input("\nPlayer, would you like to hit or stand? (h/s) ").lower()
                if hit_stand == 'h':
                    new_card = hit(deck, player)
                    print("Player takes card " + new_card.rank + new_card.suit + ". Score: " + str(player.score))
                else:
                    decision = False
            elif player.score > 21:
                print("BUSTED")
                player.bust = True
                decision = False
            else:
                decision = False


def dealer_decision(deck, dealer):
    print('\nDealer cards are: ' + get_cards(dealer) + '. Score: ' + str(dealer.score))
    decision = True
    while decision:
        if dealer.score < 17:
            new_card = hit(deck, dealer)
            print("Dealer takes card " + new_card.rank + new_card.suit + ". Score: " + str(dealer.score))
        elif 17 <= dealer.score <= 21:
            decision = False
        else:
            dealer.bust = True
            decision = False


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_ace()
    return card


def game_result(player, dealer, balance):
    payout = BlackjackPayout(balance)
    print("\nGame result:")
    if player.bust:
        print("This is a bust.")
        balance.bet_lost()
    elif dealer.bust or dealer.score < player.score:
        if player.blackjack:
            balance.bet_won(payout.blackjack())
        else:
            balance.bet_won(payout.straight())
    elif dealer.score > player.score:
        print('Dealer wins!')
        balance.bet_lost()
    elif player.score == dealer.score:
        print("This is a push. Bet is returned to player.")
    print("Total balance: " + str(balance.total))


if __name__ == "__main__":
    play_blackjack()
