import unittest
from player import Player

class TestMUDGame(unittest.TestCase):

    def test_player_initialization(self):
        player = Player()
        self.assertEqual(player.position, 0)
        self.assertEqual(player.inventory, [])

if __name__ == '__main__':
    unittest.main()
