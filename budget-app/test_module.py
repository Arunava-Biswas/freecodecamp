import unittest
import budget
from budget import create_spend_chart


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        message = 'Expected `deposit` method to create a specific object in the ledger instance variable.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        actual = self.food.ledger[0]
        expected = {"amount": 45.56, "description": ""}
        message = 'Expected calling `deposit` method with no description to create a blank description.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
        message = 'Expected `withdraw` method to create a specific object in the ledger instance variable.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_withdraw_no_description(self):
        self.food.deposit(900, "deposit")
        good_withdraw = self.food.withdraw(45.67)
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": ""}
        message1 = 'Expected `withdraw` method with no description to create a blank description.'
        message2 = 'Expected `transfer` method to return `True`.'
        try:
            self.assertEqual(actual, expected, message1)
            self.assertEqual(good_withdraw, True, message2)
        except Exception as err:
            print(err)

    def test_get_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.get_balance()
        expected = 854.33
        message = 'Expected balance to be 854.33'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        good_transfer = self.food.transfer(20, self.entertainment)
        actual = self.food.ledger[2]
        expected = {"amount": -20, "description": "Transfer to Entertainment"}
        message1 = 'Expected `transfer` method to create a specific ledger item in food object.'
        message2 = 'Expected `transfer` method to return `True`.'
        try:
            self.assertEqual(actual, expected, message1)
            self.assertEqual(good_transfer, True, message2)
        except Exception as err:
            print(err)

        actual = self.entertainment.ledger[0]
        expected = {"amount": 20, "description": "Transfer from Food"}
        message = 'Expected `transfer` method to create a specific ledger item in entertainment object.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_check_funds(self):
        self.food.deposit(10, "deposit")
        actual = self.food.check_funds(20)
        expected = False
        message = 'Expected `check_funds` method to be False'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

        actual = self.food.check_funds(10)
        expected = True
        message = 'Expected `check_funds` method to be True'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_withdraw_no_funds(self):
        self.food.deposit(100, "deposit")
        good_withdraw = self.food.withdraw(100.10)
        message = 'Expected `withdraw` method to return `False`.'
        try:
            self.assertEqual(good_withdraw, False, message)
        except Exception as err:
            print(err)

    def test_transfer_no_funds(self):
        self.food.deposit(100, "deposit")
        good_transfer = self.food.transfer(200, self.entertainment)
        message = 'Expected `transfer` method to return `False`.'
        try:
            self.assertEqual(good_transfer, False, message)
        except Exception as err:
            print(err)

    def test_to_string(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.food.transfer(20, self.entertainment)
        actual = str(self.food)
        expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
        message = 'Expected different string representation of object.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        message = 'Expected different chart representation. Check that all spacing is exact.'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    unittest.main()
