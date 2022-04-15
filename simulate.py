import sys
import time
from enum import Enum

from primercoingame import PrimerCoinGame


class Action(Enum):
    LABEL_CHEATER = -1
    LABEL_FAIR = 0
    FLIP1 = 1
    FLIP5 = 5


def generate_action(num_heads, num_tails):
    flips = num_heads + num_tails
    if flips <= 5:
        return Action.FLIP5
    elif flips < 10:
        return Action.FLIP1
    elif flips >= 10 and (num_tails == 0 or num_heads / num_tails > 1):
        return Action.LABEL_CHEATER
    else:
        return Action.LABEL_FAIR


def main(args):
    wins = 0
    pcg = PrimerCoinGame(
        starting_flips=100,
        cheater_blob_chance=0.5,
        cheater_heads_chance=0.75,
        bonus_flips=15,
        penalty_flips=30,
    )
    while pcg.flips_left > 0:
        print(pcg)
        action = generate_action(pcg.heads, pcg.tails)
        print(action, "\n")
        if action == Action.LABEL_CHEATER:
            if pcg.label_cheater():
                wins += 1
        if action == Action.LABEL_FAIR:
            if pcg.label_fair():
                wins += 1
        if action == Action.FLIP1:
            pcg.flip1()
        if action == Action.FLIP5:
            pcg.flip5()
    print(pcg)


if __name__ == "__main__":
    main(sys.argv)
