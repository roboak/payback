import unittest
from app import Game
def calculate_points_per_coupon(board, rounds, coupon_positions):
    # Function that calculates the points per coupon after a specified number of rounds
    pass  # Replace with actual implementation

class TestCalculatePointsPerCoupon(unittest.TestCase):
    def test_1st_round(self):
        board = [[0, 1, 0], [1, 0, 2], [0, 3, 0]]
        rounds = 25
        coupon_positions = {'A': (0, 0), 'B': (1, 2), 'C': (2, 1)}
        expected_points = {'A': 6, 'B': 8, 'C': 12}
        self.assertEqual(calculate_points_per_coupon(board, rounds, coupon_positions), expected_points)

    def test_50th_round(self):
        # Add test case for 50th round calculation
        pass

    def test_100th_round(self):
        # Add test case for 100th round calculation
        pass

if __name__ == '__main__':
    unittest.main()
