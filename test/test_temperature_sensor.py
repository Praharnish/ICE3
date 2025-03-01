import unittest
from src.temperature_sensor import process_temperatures

class TestTemperatureSensor(unittest.TestCase):

    # Boundary Value Analysis (BVA)
    def test_case_1(self):
        self.assertEqual(process_temperatures([-50]), "Min: -50.0°C, Max: -50.0°C, Avg: -50.00°C")

    def test_case_2(self):
        self.assertEqual(process_temperatures([150]), "Min: 150.0°C, Max: 150.0°C, Avg: 150.00°C")

    def test_case_3(self):
        self.assertEqual(process_temperatures([-49, 149]), "Min: -49.0°C, Max: 149.0°C, Avg: 50.00°C")

    # Robustness Testing
    def test_case_4(self):
        self.assertEqual(process_temperatures([-60, 20, 160]), "Out-of-bound value detected.")

    def test_case_5(self):
        self.assertEqual(process_temperatures([20, "abc", 30]), "Invalid input detected.")

    def test_case_6(self):
        self.assertEqual(process_temperatures([10, "@", -40]), "Invalid input detected.")

    # Special Scenarios
    def test_case_7(self):
        self.assertEqual(process_temperatures([2**31 - 1, -2**31]), "Out-of-bound value detected.")

    def test_case_8(self):
        self.assertEqual(process_temperatures([50, 50, 50]), "Min: 50.0°C, Max: 50.0°C, Avg: 50.00°C")

    def test_case_9(self):
        self.assertEqual(process_temperatures([]), "No input provided.")

# This block ensures that the tests run when the script is executed directly
if __name__ == "__main__":
    unittest.main()
