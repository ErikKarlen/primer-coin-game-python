from random import random


class PrimerCoinGame:

    def __init__(self, starting_flips=100, cheater_blob_chance=0.5, cheater_heads_chance=0.75, bonus_flips=15, penalty_flips=30):
        self.starting_flips = starting_flips
        self.flips_left = starting_flips
        self.cheater_blob_chance = max(0, min(cheater_blob_chance, 1))
        self.cheater_heads_chance = max(0, min(cheater_heads_chance, 1))
        self.bonus_flips = bonus_flips
        self.penalty_flips = penalty_flips
        self.rounds = 0
        self.score = 0

        self._new_round()
    
    def __str__(self):
        return f"Round: {self.rounds}\n" \
               f"Score: {self.score}\n" \
               f"Flips: {self.flips_left}\n" \
               f"Heads: {self.heads}\n" \
               f"Tails: {self.tails}\n"
    
    def __repr__(self):
        return str(self)

    def _new_round(self):
        self.rounds += 1
        self.heads = 0
        self.tails = 0
        self._current_blob_is_cheater = random() < self.cheater_blob_chance

    def _do_flips(self, num_flips):
        heads_chance = 0.5
        if self._current_blob_is_cheater:
            heads_chance = self.cheater_heads_chance
        for _ in range(num_flips):
            if random() < heads_chance:
                self.heads += 1
            else:
                self.tails += 1
            self.flips_left -= 1

    def _flipX(self, x):
        if self.flips_left < x:
            return False
        else:
            self._do_flips(x)
            return True

    def flip1(self):
        return self._flipX(1)
 
    def flip5(self):
        return self._flipX(5)

    def label_fair(self):
        correct_label = False
        if self._current_blob_is_cheater:
            self.flips_left -= self.penalty_flips
        else:
            self.flips_left += self.bonus_flips
            self.score += 1
            correct_label = True
        self._new_round()
        return correct_label

    def label_cheater(self):
        correct_label = False
        if self._current_blob_is_cheater:
            self.flips_left += self.bonus_flips
            self.score += 1
            correct_label = True
        else:
            self.flips_left -= self.penalty_flips
        self._new_round()
        return correct_label
