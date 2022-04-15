import unittest

from primercoingame import PrimerCoinGame
import primercoingame

class Test_PrimerCoinGame(unittest.TestCase):

    """
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

    def test_flip1(self):
        pcg = PrimerCoinGame(100, 0.5, 0.75, 30, 15)
        pcg.flip1()
        self.assertEqual(pcg.flips_left, 99)
    
    def test_flip5(self):
        pcg = PrimerCoinGame(100, 0.5, 0.75, 30, 15)
        pcg.flip5()
        self.assertEqual(pcg.flips_left, 95)

    def test_label_fair_correct(self):
        pcg = PrimerCoinGame(100, 0, 0.75, 30, 15)
        self.assertTrue(pcg.label_fair())

    def test_label_fair_wrong(self):
        pcg = PrimerCoinGame(100, 1, 0.75, 30, 15)
        self.assertFalse(pcg.label_fair())

    def test_label_cheater_correct(self):
        pcg = PrimerCoinGame(100, 1, 0.75, 30, 15)
        self.assertTrue(pcg.label_cheater())

    def test_label_cheater_wrong(self):
        pcg = PrimerCoinGame(100, 0, 0.75, 30, 15)
        self.assertFalse(pcg.label_cheater())
