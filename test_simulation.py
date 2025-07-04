
import unittest
from car import Car
from engine import run_simulation

class TestDrivingSimulation(unittest.TestCase):

    def test_single_car_simple_path(self):
        car = Car("A", 1, 2, "N", "FFRFFFFRRL")
        result = run_simulation([car], 10, 10)
        self.assertIn("- A, (5,4) S", result)

    def test_prevent_out_of_bounds(self):
        car = Car("B", 0, 0, "S", "FFF")
        result = run_simulation([car], 5, 5)
        self.assertIn("- B, (0,0) S", result)

    def test_detect_collision_between_cars(self):
        car1 = Car("A", 1, 2, "N", "FFRFFFFRRL")
        car2 = Car("B", 7, 8, "W", "FFLFFFFFFF")
        result = run_simulation([car1, car2], 10, 10)
        self.assertTrue(any("collides" in line for line in result))

    def test_no_move_command(self):
        car = Car("C", 3, 3, "E", "")
        result = run_simulation([car], 5, 5)
        self.assertIn("- C, (3,3) E", result)

    def test_off_grid_starting_point(self):
        car = Car("X", 100, 100, "N", "F")
        result = run_simulation([car], 10, 10)
        self.assertIn("- X, (100,100) N", result)

    def test_multiple_collisions_possible(self):
        car1 = Car("A", 0, 0, "E", "FF")
        car2 = Car("B", 4, 0, "W", "FF")
        car3 = Car("C", 2, 2, "S", "FF")
        result = run_simulation([car1, car2, car3], 5, 5)
        collisions = [line for line in result if "collides" in line]
        self.assertGreaterEqual(len(collisions), 3)

    def test_invalid_commands_ignored(self):
        car = Car("Z", 1, 1, "N", "ABCXYZ")
        result = run_simulation([car], 5, 5)
        self.assertIn("- Z, (1,1) N", result)

    
    def test_overlapping_start_position(self):
        # Two cars move toward same spot (3,2) to trigger collision
        car1 = Car("A", 2, 2, "E", "F")  # Moves to (3,2)
        car2 = Car("B", 4, 2, "W", "F")  # Moves to (3,2)
        result = run_simulation([car1, car2], 5, 5)
        self.assertTrue(any("collides" in line for line in result))

    def test_unequal_command_lengths(self):
        car1 = Car("A", 0, 0, "E", "FF")
        car2 = Car("B", 1, 0, "E", "FFFFFF")
        result = run_simulation([car1, car2], 10, 10)
        self.assertIn("- A, (2,0) E", result)
        self.assertTrue(any("B" in line for line in result))

    def test_circular_path_returns_to_origin(self):
        car = Car("Loop", 2, 2, "N", "RFRFRFRF")
        result = run_simulation([car], 5, 5)
        self.assertIn("- Loop, (2,2) N", result)

    def test_no_cars_added(self):
        result = run_simulation([], 5, 5)
        self.assertEqual(result, [])

    def test_long_command_string(self):
        car = Car("Longy", 0, 0, "N", "F"*500 + "L"*100 + "R"*100)
        result = run_simulation([car], 50, 50)
        self.assertTrue(any("Longy" in line for line in result))

if __name__ == '__main__':
    unittest.main()
