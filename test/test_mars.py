import unittest
from mars import Mars


class MarsEdgesTest(unittest.TestCase):
    def test_negative_locations_off_map(self):
        mars = Mars(3, 5)
        self.assertFalse(mars.location_exists(3, -2))

    def test_locations_too_great_off_map(self):
        mars = Mars(6, 2)
        self.assertFalse(mars.location_exists(7, 1))
        self.assertFalse(mars.location_exists(6, 3))

    def test_valid_locations_recognised(self):
        mars = Mars(2, 1)
        self.assertTrue(mars.location_exists(1, 1))
        self.assertTrue(mars.location_exists(0, 1))


class MarsScentingTest(unittest.TestCase):
    def setUp(self):
        self.mars = Mars(5, 5)

    def test_unscented_locations_return_false(self):
        self.assertFalse(self.mars.location_is_scented(1, 2))
        self.assertFalse(self.mars.location_is_scented(-1, 4))
        self.assertFalse(self.mars.location_is_scented(7, 6))

    def test_adding_scented_locations(self):
        self.mars.add_scented_location(2, 2)
        self.assertEqual(self.mars.scented_locations, [[2, 2], ])

    def test_scented_locations_return_true(self):
        self.mars.scented_locations = [[2, 2], ]
        self.assertTrue(self.mars.location_is_scented(2, 2))

        self.mars.add_scented_location(1, 3)
        self.assertTrue(self.mars.location_is_scented(1, 3))
