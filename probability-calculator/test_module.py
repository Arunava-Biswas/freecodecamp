import unittest
import prob_calculator

prob_calculator.random.seed(95)


class UnitTests(unittest.TestCase):
    def test_hat_class_contents(self):
        hat = prob_calculator.Hat(red=3, blue=2)
        actual = hat.contents
        expected = ["red", "red", "red", "blue", "blue"]
        message = 'Expected creation of hat object to add correct contents.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_hat_draw(self):
        hat = prob_calculator.Hat(red=5, blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        message1 = 'Expected hat draw to return two random items from hat contents.'
        try:
            self.assertEqual(actual, expected, message1)
        except Exception as err:
            print(err)
        actual = len(hat.contents)
        expected = 5
        message2 = 'Expected hat draw to reduce number of items in contents.'
        try:
            self.assertEqual(actual, expected, message2)
        except Exception as err:
            print(err)

    def test_prob_experiment(self):
        hat = prob_calculator.Hat(blue=3, red=2, green=6)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.272
        try:
            self.assertAlmostEqual(actual, expected, delta=0.01, msg='Expected experiment method to return a different probability.')
        except Exception as err:
            print(err)
        hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow": 2,"blue": 3,"test": 1}, num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        try:
            self.assertAlmostEqual(actual, expected, delta=0.01, msg='Expected experiment method to return a different probability.')
        except Exception as err:
            print(err)


if __name__ == "__main__":
    unittest.main()
