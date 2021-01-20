from RPS_game import mrugesh, abbey, quincy, kris


def play(player1, player2, num_games):

    player1_hist = {}
    player2_hist = {}
    hist = []
    p1_prev_play = ""
    p2_prev_play = ""

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        player1_hist[_] = p1_play
        player2_hist[_] = p2_play



    hist.append(player1_hist)
    hist.append(player2_hist)

    return hist


def player(prev_opponent_play, opponent_history=[], player_history=[]):

    guess = ''

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    if len(opponent_history) <= 10:
        guess = ['R', 'S'][len(opponent_history) % 2]
    if len(opponent_history) <= 15:
        guess = ['R', 'P'][len(opponent_history) % 2]

    if guess == '':
        guess = 'R'

    player_history.append(guess)

    return guess


quincy = play(player, quincy, 15)
abbey = play(player, abbey, 15)
kris = play(player, kris, 15)
mrugesh = play(player, mrugesh, 15)

print(quincy)
print(abbey)
print(kris)
print(mrugesh)
