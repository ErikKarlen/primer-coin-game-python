import sys
from enum import Enum

from primercoingame import PrimerCoinGame


class Action(Enum):
    LABEL_CHEATER = -1
    LABEL_FAIR = 0
    FLIP1 = 1
    FLIP5 = 5


def generate_action(num_heads, num_tails):
    """
    Generates an action given the current number of heads and tails

    Parameters
    ----------
    num_heads : int
        Number of heads seen so far for current blob
    num_tails : int
        Number of tails seen so far for current blob
    """
    num_flips = num_heads + num_tails
    if num_flips <= 5:
        return Action.FLIP5
    elif num_flips < 10:
        return Action.FLIP1
    elif num_flips >= 10 and (num_tails == 0 or num_heads / num_tails > 1):
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
    pcg = PrimerCoinGame(
        starting_flips=100,
        cheater_blob_chance=0.5,
        cheater_heads_chance=0.75,
        bonus_flips=15,
        penalty_flips=30,
    )
    while pcg.flips_left > 0:
        action = generate_action(pcg.heads, pcg.tails)
        if action == Action.LABEL_CHEATER:
            pcg.label_cheater()
        if action == Action.LABEL_FAIR:
            pcg.label_fair()
        if action == Action.FLIP1:
            pcg.flip1()
        if action == Action.FLIP5:
            pcg.flip5()
    print(f"Final Score: {pcg.score}")


if __name__ == "__main__":
    main(sys.argv)
