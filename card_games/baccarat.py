from card_games.core.balance import BaccaratBalance, BaccaratPayout
from card_games.core.deck import BaccaratDeck
from card_games.core.hands import Hand
from terminaltables import SingleTable
from pick import pick
import os

cls = lambda: os.system('clear')


def play_baccarat():
    balance = BaccaratBalance()
    cls()
    table_data = [
        ['    PLAYER    ', '    BANKER    '],
        ['Player pays', '1:1'],
        ['Tie pays', '8:1'],
        ['Banker pays', '0.95:1'],
        ['Total balance', str(balance.total)]
    ]
    table_instance = SingleTable(table_data, '[ BACCARAT ]')
    table_instance.justify_columns = {0: 'right', 1: 'left'}
    print(table_instance.table)

    # prepare deck and balance
    deck = BaccaratDeck()
    deck.build()
    deck.shuffle()
    balance = BaccaratBalance()

    input("Press any key to start")

    is_playing = True
    while is_playing:
        # prepare hands
        player = Hand()
        banker = Hand()

        place_bets(balance)

        deal_initial_cards(deck, player, banker)
        p3_card = process_3rd_card_player(deck, player)
        b3_card = process_3rd_card_banker(deck, banker, p3_card)

        table_data = [
            ['    PLAYER [' + str(player.score) + ']', '[' + str(banker.score) + '] BANKER    '],
            [str(p3_card) + str(player.cards[0]) + str(player.cards[1]),
             str(banker.cards[0]) + str(banker.cards[1]) + str(b3_card)]
        ]
        table_instance = SingleTable(table_data, '[ BACCARAT ]')
        table_instance.justify_columns = {0: 'right', 1: 'left'}
        cls()
        print(table_instance.table)

        game_result(player, banker, balance)

        next_round = input("\nWould you like to play again? \nPress any key to continue or 'q' to quit:").lower()
        if next_round != 'q':
            continue
        else:
            is_playing = False


def place_bets(balance):
    balance.flush_bets()
    player_bet = balance.player_bet
    tie_bet = balance.tie_bet
    banker_bet = balance.banker_bet
    placing_bet = True
    while placing_bet:
        title = 'Please place your bets: '
        options = ['Deal now!', 'Player ' + str(player_bet), 'Tie ' + str(tie_bet), 'Banker ' + str(banker_bet)]
        option, index = pick(options, title)
        if index == 0:
            placing_bet = False
        elif index == 1:
            player_bet += select_chip()
            balance.player_bet += player_bet
            balance.total -= player_bet
        elif index == 2:
            tie_bet += select_chip()
            balance.tie_bet += tie_bet
            balance.total -= tie_bet
        elif index == 3:
            banker_bet += select_chip()
            balance.banker_bet += banker_bet
            balance.total -= banker_bet


def select_chip():
    title = 'Please select chip: '
    options = ['5', '10', '25', '50', '100']
    option, index = pick(options, title)
    if index == 0:
        return 5
    elif index == 1:
        return 10
    elif index == 2:
        return 25
    elif index == 3:
        return 50
    elif index == 4:
        return 100


def deal_initial_cards(deck, player, banker):
    deal_card(deck, player)
    deal_card(deck, banker)
    deal_card(deck, player)
    deal_card(deck, banker)


def process_3rd_card_player(deck, player):
    if player.score < 6:
        return deal_card(deck, player)
    else:
        return '  '


def process_3rd_card_banker(deck, banker, p3_card):
    if ((0 <= banker.score < 3) or
            (banker.score == 3 and p3_card != 8) or
            (banker.score == 4 and p3_card not in [0, 1, 8, 9]) or
            (banker.score == 5 and p3_card not in [0, 1, 2, 3, 8, 9]) or
            (banker.score == 6 and p3_card in [8, 9])):
        return deal_card(deck, banker)
    else:
        return '  '


def deal_card(deck, hand):
    if len(deck.deck) < 15:
        deck.build()
        deck.shuffle()
        print('New deck has been shuffled')
    card = deck.deal()
    hand.add_card(card)
    if hand.score >= 10:
        hand.score -= 10
    return card


def game_result(player, banker, balance):
    payout = BaccaratPayout(balance)
    if player.score > banker.score:
        print("Player wins!")
        balance.bet_won(payout.player())
    elif player.score < banker.score:
        print("Banker wins!")
        balance.bet_won(payout.banker())
    else:
        print("Tie!")
        balance.bet_won(payout.tie())
    print('Total balance: ' + str(balance.total))


if __name__ == "__main__":
    play_baccarat()
