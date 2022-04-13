from enum import Enum
from random import randrange, random


class Action(Enum):
    FLIP_1 = 0
    FLIP_5 = 1
    LABEL_FAIR = 2
    LABEL_CHEATER = 3


class GameState(Enum):
    PLAYING = 0
    GAME_OVER = 1
    GAME_WIN = 2


class PrimerCoinGame:

    def __init__(self, flips=100, cheater_chance=0.5, bonus_flips=15, penalty_flips=30):
        self.flips = flips
        self.cheater_chance = cheater_chance
        self.bonus_flips = bonus_flips
        self.penalty_flips = penalty_flips
        self.rounds = 0
        self.score = 0
        self.heads = 0
        self.tails = 0
        self.game_state = GameState.PLAYING
        self.new_round()

    def new_round(self):
        self.rounds += 1
        self.current_blob_is_cheater = random() < self.cheater_chance

    def check_game_state(self):
        if self.flips <= 0:
            self.rounds += 1
            self.game_state = GameState.GAME_OVER

    def flip(self, num_flips=1):
        for _ in range(num_flips):
            if (randrange(0, 2)):
                self.heads += 1
            else:
                self.tails += 1
            self.flips -= 1
            self.check_game_state()

    def handle_action(self, action: Action):
        if action == Action.FLIP_1:
            self.flip()
        elif action == Action.FLIP_5:
            self.flip(num_flips=5)
        elif action == Action.LABEL_FAIR:
            if self.current_blob_is_cheater:
                self.flips -= self.penalty_flips
                self.check_game_state()
            else:
                self.score += 1
            self.new_round()
        elif action == Action.LABEL_CHEATER:
            if self.current_blob_is_cheater:
                self.score += 1
                self.game_state = GameState.GAME_WIN
            else:
                self.game_state = GameState.GAME_OVER
            self.new_round()

        return self.game_state