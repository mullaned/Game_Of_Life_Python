import unittest

from Game_Of_Life import test

class Test_Game_Of_Life(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(test(1),1)
