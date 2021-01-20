# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago.
# It is not a very good player so you will need to change the code to pass the challenge.
import random

"""
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if (opponent_history[-1] == 'R' and opponent_history[-2]== 'S'):
      guess = 'P'
    elif (opponent_history[-1] == 'R'):
      guess == 'S'
    else:
      guess = 'P' 

    return guess
    """


def player(prev_opponent_play, opponent_history=[], player_history=[],
           options=[{'RR': 0, 'RP': 0, 'RS': 0, 'PR': 0, 'PP': 0, 'PS': 0, 'SR': 0, 'SP': 0, 'SS': 0}]):

    guess = ''

    base_options = ['R', 'P', 'S']
    response = {'P': 'S', 'R': 'P', 'S': 'R'}
    opponent_first_moves = [['R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R'],
                            ['R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'S'],
                            ['R', 'P', 'S', 'P', 'S', 'P', 'S', 'P', 'S', 'P', 'S'],
                            ['R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']]

    if len(opponent_history) >= 15:

        if opponent_history[0:11] == opponent_first_moves[0] or opponent_history[0:11] == opponent_first_moves[1]:

            if prev_opponent_play == '':
                prev_opponent_play = "S"
            guess = response[prev_opponent_play]

        elif opponent_history[0:11] == opponent_first_moves[2]:

            if len(opponent_history) > 1:

                if player_history[-1] == opponent_history[-1]:
                    guess = random.choice(base_options)
                elif player_history[-1] == 'R':
                    guess = 'S' if opponent_history[-1] == 'S' else 'P'
                elif player_history[-1] == 'P':
                    guess = 'R' if opponent_history[-1] == 'R' else 'S'
                else:
                    guess = 'P' if opponent_history[-1] == 'P' else 'R'

        elif opponent_history[0:11] == opponent_first_moves[3]:

            two_last_opponent_play = ''.join(player_history[-2:])

            if len(two_last_opponent_play) == 2:
                options[0][two_last_opponent_play] += 1

            plays_options = [player_history[-1] + 'R', player_history[-1] + 'P', player_history[-1] + 'S']

            mask = {p: options[0][p] for p in plays_options if p in options[0]}

            prediction = max(mask, key=mask.get)[-1:]

            if len(opponent_history) % 2:
                response = {'P': 'R', 'R': 'S', 'S': 'P'}

            guess = response[prediction]

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    if len(opponent_history) <= 15:
        if len(opponent_history) <= 10:
            guess = ['R', 'S'][len(opponent_history) % 2]
        if len(opponent_history) <= 15:
            guess = ['R', 'P'][len(opponent_history) % 2]

    if guess == '':
        guess = 'R'

    player_history.append(guess)

    if len(opponent_history) == 1000 or len(player_history) == 1000:
        opponent_history.clear()
        player_history.clear()

    return guess
