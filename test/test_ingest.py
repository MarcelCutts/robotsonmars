import unittest
import ingest


class InitialCoordinateTest(unittest.TestCase):
    def test_out_of_range_coordinates_causes_exit(self):
        with self.assertRaises(SystemExit):
            ingest.extract_coordinates("100 0")
        with self.assertRaises(SystemExit):
            ingest.extract_coordinates("5 -10")

    def test_non_integer_coordinates_causes_exit(self):
        with self.assertRaises(SystemExit):
            ingest.extract_coordinates("10 p")

    def test_correct_ranges_produce_correct_result(self):
        result = ingest.extract_coordinates("0 10")
        self.assertEqual(result, {'maximum_x': 0, 'maximum_y': 10})


class RobotInstructionsTest(unittest.TestCase):
    def test_too_many_instructions_cause_system_error(self):
        oversized_instructions = ["3 2 N", "LR" * 200]
        with self.assertRaises(SystemExit):
            ingest.extract_robots_instructions(oversized_instructions)

    def test_valid_instructions_generates_correct_output(self):
        valid_instructions = ["3 2 N", "LR"]
        result = ingest.extract_robots_instructions(valid_instructions)
        self.assertEqual(result, [{
            'initial_x': 3,
            'initial_y': 2,
            'initial_orientation': 'N',
            'movement_instructions': 'LR',
            }])


class FileReadingTest(unittest.TestCase):
    def test_unknown_file_(self):
        with self.assertRaises(SystemExit):
            ingest.ingest_from_file('doesntexists.txt')

    def test_valid_file_passes(self):
        result = ingest.ingest_from_file('test/sample_instructions.txt')
        self.assertIsInstance(result, tuple)


if __name__ == '__main__':
    unittest.main()
