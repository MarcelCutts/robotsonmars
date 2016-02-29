import unittest
from robot import Robot

class TestMoving(unittest.TestCase):
    def test_move_forward_north(self):
        north_bot = Robot(5, 5, 'N', 'F')
        north_bot.move_forward()
        self.assertEqual(north_bot.current_x, 5)
        self.assertEqual(north_bot.current_y, 6)

    def test_move_forward_east(self):
        north_bot = Robot(11, 7, 'E', 'F')
        north_bot.move_forward()
        self.assertEqual(north_bot.current_x, 12)
        self.assertEqual(north_bot.current_y, 7)

    def test_move_forward_south(self):
        north_bot = Robot(3, 4, 'S', 'F')
        north_bot.move_forward()
        self.assertEqual(north_bot.current_x, 3)
        self.assertEqual(north_bot.current_y, 3)

    def test_move_forward_west(self):
        north_bot = Robot(1, 0, 'W', 'F')
        north_bot.move_forward()
        self.assertEqual(north_bot.current_x, 0)
        self.assertEqual(north_bot.current_y, 0)


class TestTurning(unittest.TestCase):
    def test_turn_left_from_north(self):
        north_bot = Robot(5, 5, 'N', 'L')
        north_bot.turn('L')
        self.assertEqual(north_bot.current_orientation, 'W')

    def test_turn_right_from_north(self):
        north_bot = Robot(5, 5, 'N', 'R')
        north_bot.turn('R')
        self.assertEqual(north_bot.current_orientation, 'E')

    def test_turn_left_from_east(self):
        north_bot = Robot(5, 5, 'E', 'L')
        north_bot.turn('L')
        self.assertEqual(north_bot.current_orientation, 'N')

    def test_turn_right_from_east(self):
        north_bot = Robot(5, 5, 'E', 'R')
        north_bot.turn('R')
        self.assertEqual(north_bot.current_orientation, 'S')

    def test_turn_left_from_south(self):
        north_bot = Robot(5, 5, 'S', 'L')
        north_bot.turn('L')
        self.assertEqual(north_bot.current_orientation, 'E')

    def test_turn_right_from_south(self):
        north_bot = Robot(5, 5, 'S', 'R')
        north_bot.turn('R')
        self.assertEqual(north_bot.current_orientation, 'W')

    def test_turn_left_from_west(self):
        north_bot = Robot(5, 5, 'W', 'L')
        north_bot.turn('L')
        self.assertEqual(north_bot.current_orientation, 'S')

    def test_turn_right_from_west(self):
        north_bot = Robot(5, 5, 'W', 'R')
        north_bot.turn('R')
        self.assertEqual(north_bot.current_orientation, 'N')
