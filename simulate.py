import sys
from enum import Enum

from primercoingame import PrimerCoinGame


class Action(Enum):
    LABEL_CHEATER = -1
    LABEL_FAIR = 0
    FLIP1 = 1
    FLIP5 = 5


def generate_action(flips_left, num_heads, num_tails):
    """
    Generates an action given the current number of heads and tails

    Parameters
    ----------
    flips_left : int
        Number of flips left the player has
    num_heads : int
        Number of heads seen so far for current blob
    num_tails : int
        Number of tails seen so far for current blob
    """
    num_flips = num_heads + num_tails
    if flips_left >= 5 and num_flips < 5:
        return Action.FLIP5
    elif flips_left >= 1 and num_flips < 12:
        return Action.FLIP1
    elif num_tails == 0 or num_heads / num_tails > 1:
        return Action.LABEL_CHEATER
    else:
        return Action.LABEL_FAIR


def main(args):
    """
    The main function for simulating the Primer Coin Game

    Parameters
    ----------
    args : list
        list of input arguments
    """
    num_games = 1000
    max_score = 0
    for _ in range(num_games):
        pcg = PrimerCoinGame(
            starting_flips=100,
            cheater_blob_chance=0.5,
            cheater_heads_chance=0.75,
            bonus_flips=15,
            penalty_flips=30,
        )
        while pcg.flips_left >= 0 and not (
            pcg.flips_left == pcg.heads == pcg.tails == 0
        ):
            action = generate_action(pcg.flips_left, pcg.heads, pcg.tails)
            if action == Action.LABEL_CHEATER:
                pcg.label_cheater()
            elif action == Action.LABEL_FAIR:
                pcg.label_fair()
            elif action == Action.FLIP1:
                pcg.flip1()
            elif action == Action.FLIP5:
                pcg.flip5()
        if pcg.score > max_score:
            max_score = pcg.score
    print(f"Max Score: {max_score}")


if __name__ == "__main__":
    main(sys.argv)
