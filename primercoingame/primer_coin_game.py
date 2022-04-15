from random import random


class PrimerCoinGame:
    """
    A class used to simulate in Python the Coin Game developed by
    Primer.

    In the game there is a blob that is either fair or a cheater and the
    goal of the player is to guess which one the blob is. To find this
    out the player can let the blob flip coins and see the results of
    the flips. For every correct label the player gives it receives 
    bonus flips and for every incorrect it is penalised with losing some
    flips. The player starts with a limited number of initial flips.

    The original game created by Primer starts the player with 100 flips
    and the bonus and penalty flips are set to 15 and 30 respectively.

    Primer has made a video with details about the game which you can
    find here: https://www.youtube.com/watch?v=QC91Bf8hQVo

    Attributes
    ----------
    starting_flips : int
        number of flips the player starts with
    flips_left : int
        number of flips the player has left
    cheater_blob_chance : float
        probability that a blob is a cheater
    cheater_heads_chance : float
        probability that a cheater flips head
    bonus_flips : int
        number of flips the player gets for a correct guess
    penalty_flips : int
        number of flips the player loses for an incorrect guess
    rounds : int
        number of rounds the game has lasted
    score : int
        number of times the player correctly labelled the blobs
    heads : int
        number of times the current blob flipped heads
    tails : int
        number of times the current blob flipped tails

    Methods
    -------
    flip1()
        Make the current blob flip a coin once
    flip5()
        Make the current blob flip a coin five times
    label_fair()
        Guess the current blob is fair and start a new round
    label_cheater()
        Guess the current blob is a cheater and start a new round
    """

    def __init__(
        self,
        starting_flips: int,
        cheater_blob_chance: float,
        cheater_heads_chance: float,
        bonus_flips: int,
        penalty_flips: int,
    ):
        """
        Parameters
        ----------
        starting_flips : int
            The number of flips the player starts with
        cheater_blob_chance : float
            The chance that a blob will be a cheater
        cheater_heads_chance : float
            The chance that a cheater will flip a head
        bonus_flips : int
            The number of flips the player gets for a correct guess
        penalty_flips : int
            The number of flips the player will lose for a wrong guess
        """
        self.starting_flips = starting_flips
        self.flips_left = starting_flips
        self.cheater_blob_chance = max(0, min(cheater_blob_chance, 1))
        self.cheater_heads_chance = max(0, min(cheater_heads_chance, 1))
        self.bonus_flips = bonus_flips
        self.penalty_flips = penalty_flips
        self.rounds = 0
        self.score = 0

        self._new_round()

    def __str__(self) -> str:
        return (
            f"Round: {self.rounds}\n"
            f"Score: {self.score}\n"
            f"Flips: {self.flips_left}\n"
            f"Heads: {self.heads}\n"
            f"Tails: {self.tails}\n"
        )

    def __repr__(self) -> str:
        return str(self)

    def _new_round(self):
        """
        Start a new round
        """
        self.rounds += 1
        self.heads = 0
        self.tails = 0
        self._current_blob_is_cheater = random() < self.cheater_blob_chance

    def _do_flips(self, num_flips: int):
        """
        Do a flip a total of num_flips times
        """
        heads_chance = 0.5
        if self._current_blob_is_cheater:
            heads_chance = self.cheater_heads_chance
        for _ in range(num_flips):
            if random() < heads_chance:
                self.heads += 1
            else:
                self.tails += 1
            self.flips_left -= 1

    def _flipX(self, x: int) -> bool:
        """
        Flip x times and return True if there are more flips left
        """
        if self.flips_left < x:
            return False
        else:
            self._do_flips(x)
            return True

    def flip1(self) -> bool:
        """
        Make the current blob do a coin flip

        Returns
        -------
        bool
            True if there are more flips left
        """
        return self._flipX(1)

    def flip5(self) -> bool:
        """
        Make the current blob do five coin flips

        Returns
        -------
        bool
            True if there are more flips left
        """
        return self._flipX(5)

    def label_fair(self) -> bool:
        """
        Guess that the current blob is fair

        If correct increase the score by one and add bonus_flips to
        flips_left. If incorrect remove penalty_flips from flips_left.
        Then start a new round.

        Returns
        -------
        bool
            True if the current blob was fair
        """
        correct_label = False
        if self._current_blob_is_cheater:
            self.flips_left -= self.penalty_flips
        else:
            self.flips_left += self.bonus_flips
            self.score += 1
            correct_label = True
        self._new_round()
        return correct_label

    def label_cheater(self) -> bool:
        """
        Guess that the current blob is a cheater

        If correct increase the score by one and add bonus_flips to
        flips_left. If incorrect remove penalty_flips from flips_left.
        Then start a new round.

        Returns
        -------
        bool
            True if the current blob was a cheater
        """
        correct_label = False
        if self._current_blob_is_cheater:
            self.flips_left += self.bonus_flips
            self.score += 1
            correct_label = True
        else:
            self.flips_left -= self.penalty_flips
        self._new_round()
        return correct_label
