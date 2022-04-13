import sys

from primercoingame import PrimerCoinGame, Action, GameState


def generate_action(num_heads, num_tails):
    print(f"heads: {num_heads}")
    print(f"tails: {num_tails}\n")
    return Action.LABEL_CHEATER

def main(args):
    rounds = 10
    pcg = PrimerCoinGame(cheater_chance=0.1)
    for _ in range(rounds):
        while pcg.game_state == GameState.PLAYING:
            res = pcg.handle_action(generate_action(pcg.heads, pcg.tails))
    print(pcg.score)

if __name__ == "__main__":
    main(sys.argv)