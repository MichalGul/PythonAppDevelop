
import unittest
from knight import Knight
from hut import Hut

class TestHut(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()

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

if __name__ =='main':
    unittest.main()


