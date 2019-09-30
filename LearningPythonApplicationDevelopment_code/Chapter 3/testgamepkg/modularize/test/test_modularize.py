import sys

sys.path.append('../')

import unittest

from knight import Knight
from orcrider import OrcRider
from abstractgameunit import AbstractGameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs
from unittest import mock

class TestWarGame(unittest.TestCase):
    """This class contains unit test for the game Attack of the Orcs"""


    def setUp(self):
        """Overrides the setUp fixture of the superclass"""
        self.knight = Knight()
        self.enemy = OrcRider()

    @unittest.skip("reason for skipping")
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


    def test_play(self):
        """Unit test to veryfy AttackOfTheOrcs
        """
        game = AttackOfTheOrcs()
        self.hut_selection_counter = 0
        #Zastepowanie wbudowanej funkcji 'input' nasza funkcja
        with mock.patch('builtins.input', new = self.user_input_processor):
            game.play()

            #Create a list that collects information on whether the huts are acquired. Boolean list
            acquired_hut_list = [h.is_acquired for h in game.huts]

            #Player wins if all huts are acquired AND the player health is greather than 0
            if all(acquired_hut_list):
                #All the huts are acquired (winning criteria)
                #check the player's health!
                self.assertTrue(game.player.health_meter > 0)
            else:
                #Losing criteria. Player health can not be positive when he losses
                self.assertFalse(game.player.health_meter > 0)

    def test_occupy_huts(self):
        game = AttackOfTheOrcs()
        game.setup_game_scenario()

        # Veryfi that only 5 huts are created
        self.assertEqual(len(game.huts), 5)

        # Huts occupants must be an instance of the Knight or OrcRider
        # or it could be set to None
        for hut in game.huts:
            assert((hut.occupant is None) or
                isinstance(hut.occupant, AbstractGameUnit))

    def user_input_processor(self, prompt):
        """Simulate user input based on user prompt
        
        :param prompt: The question asked to the user
        :type prompt: The simulated user input

        The prompt cam be either of the following:
        1. choose a hut number to enter (1-5)
        2. continue attack? (y/n)
        """
        # Check if some keywords exist in the prompt

        if 'hut' in prompt.lower():
            #Asking for hut nuimber
            print("asked for hut")
            self.hut_selection_counter += 1
            assert self.hut_selection_counter <= 5
            return self.hut_selection_counter
        elif 'attack' in prompt.lower():
            print("Asked for fight")
            return 'y'
        else:
            raise Exception("Got an unexpected prompt!", prompt)



if __name__ == '__main__':
    unittest.main()