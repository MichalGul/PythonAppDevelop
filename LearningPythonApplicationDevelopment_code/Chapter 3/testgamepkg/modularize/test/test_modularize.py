import unittest

from knight import Knight
from orcrider import OrcRider
from abstractgameunit import AbstractGameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs

class TestWarGame(unittest.TestCase):
    """This class contains unit test for the game Attack of the Orcs"""


    def setUp(self):
        """Overrides the setUp fixture of the superclass"""
        self.knight = Knight()
        self.enemy = OrcRider()

    def test_injured_unit_selection(self):
        """ Unit test to veryfy working of weighted_random_selection """
        pass

if __name__ == '__main__':
    unittest.main()Za