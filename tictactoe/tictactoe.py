import random
import os

# this would be used to clear output between rounds
cls = lambda: os.system('clear')


def start_game():
    player1 = {"name": "empty", "side": "empty", "score": 0}
    player2 = {"name": "empty", "side": "empty", "score": 0}
    print("Game of Tic Tac Toe has begun! Choose your steps wisely.")
    player1['name'] = input("Player1, please enter your name and press [Enter]:").lower().capitalize()
    print(player1['name'])
    player2['name'] = input("Player2, please enter your name and press [Enter]:").lower().capitalize()
    print(player2['name'])
    print("Now RNG system will select sides and whom to make first step")
    players = [player1, player2]
    random.shuffle(players)
    players[0]['side'], players[1]['side'] = "X", "O"
    print(player1['name'] + " side is: '" + player1['side'] + "' and " + player2['name'] + " side is: '" + player2[
        'side'] + "'")
    random.shuffle(players)
    print("Player '" + players[0]['name'] + "' goes first!")
    input("Are you ready to start (y/n)?")
    is_game_running = True
    while is_game_running:
        marks = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
        round_count = 1
        is_round_running = True
        while is_round_running:
            cls()
            draw_table(marks)
            move_running = True
            while move_running:
                move = input("Please select cell to put mark")
                if marks[move] is not " ":
                    print("This cell has already been taken")
                else:
                    marks[move] = players[0]['side']
                    move_running = False
            if round_count < 4:
                round_count += 1
                players.reverse()
                continue
            elif round_count == 9:
                print("Round resulted in a draw.")
                player1['score'] += 2
                player2['score'] += 2
                is_round_running = False
            else:
                round_outcome = calculate_win(marks, players[0]['side'])
                if round_outcome:
                    print("Round finished! Player '" + players[0]['name'] + "' won!")
                    players[0]['score'] += 3
                    players[1]['score'] += 1
                    is_round_running = False
                else:
                    round_count += 1
                    players.reverse()
                    continue

        print("\nCurrent score:")
        print("Player '" + player1['name'] + "' has '" + str(player1['score']) + "' points")
        print("Player '" + player2['name'] + "' has '" + str(player2['score']) + "' points")
        to_continue = input("\nWould you like to continue (y/n)?").lower()
        if to_continue == 'y':
            continue
        else:
            is_game_running = False
    print("\nGAME OVER!\nThanks for playing! =)")


def calculate_win(marks, side):
    return (
            (marks['1'] == marks['2'] == marks['3'] == side) or
            (marks['4'] == marks['5'] == marks['6'] == side) or
            (marks['7'] == marks['8'] == marks['9'] == side) or
            (marks['1'] == marks['4'] == marks['7'] == side) or
            (marks['2'] == marks['5'] == marks['8'] == side) or
            (marks['3'] == marks['6'] == marks['9'] == side) or
            (marks['1'] == marks['5'] == marks['9'] == side) or
            (marks['7'] == marks['5'] == marks['3'] == side)
    )


def draw_table(marks):
    vertical = '   |   |   '
    horizontal = '___|___|___'
    row3 = ' ' + marks['7'] + ' | ' + marks['8'] + ' | ' + marks['9'] + ' '
    row2 = ' ' + marks['4'] + ' | ' + marks['5'] + ' | ' + marks['6'] + ' '
    row1 = ' ' + marks['1'] + ' | ' + marks['2'] + ' | ' + marks['3'] + ' '
    print(vertical)
    print(row3)
    print(horizontal)
    print(vertical)
    print(row2)
    print(horizontal)
    print(vertical)
    print(row1)
    print(vertical)


if __name__ == "__main__":
    start_game()
