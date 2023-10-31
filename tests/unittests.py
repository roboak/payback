import unittest
from unittest.mock import MagicMock
from src.app import Game


class TestGame(unittest.TestCase):
    # def test_get_number_of_points_per_each_coupon(self):
    #     # Create a Game instance with known parameters
    #     g = Game(2, 1)
    #
    #     # Call the method to get number of points per coupon
    #     result = g.get_number_of_points_per_each_coupon()
    #
    #     # Add your assertions here to check if the result is as expected
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result), 2)  # Ensure the result has the expected length
    #     # You can add more specific assertions based on the behavior of your code

    def test_get_max_coupons(self):
        # Create a Game instance with known parameters
        g = Game(2, 1)

        # Call the method to get max coupons
        g.board._get_random_choice = MagicMock()

        # Set the return value for random.choice
        g.board._get_random_choice.return_value = (1, 0)  # Replace with your expected values

        g.simulate()
        # g.get_number_of_points_per_each_coupon()
        ans=g.get_max_coupons()

        # Add your assertions here to check if the result is as expected
        self.assertIsInstance(ans, list)
        # You can add more specific assertions based on the behavior of your code
        self.assertEqual(1,g.board.get_coupons()[ans[0][0]][ans[0][1]].value)

if __name__ == '__main__':
    unittest.main()