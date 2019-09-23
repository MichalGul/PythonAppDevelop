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
        for i in range(1000):
            injured_unit = weighted_random_selection(self.knight, self.enemy)

            self.assertIsInstance(injured_unit, AbstractGameUnit, "Injured unit must be an instance of AbstractGameUnit")


    def test_acquire_hut(self):
        """
        Unittest to veryfie hut occupant after it is acquired

        Unit test to ensure that when hut is acquired, the
        hut.occupant is updated to the Knight instance
        """
        print("\n Calling test_hut.test_acquire_hut")
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)

if __name__ == '__main__':
    unittest.main()