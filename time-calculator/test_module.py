import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):

    def test_period_same(self):
        actual = add_time("1:30 PM", "3:25")
        expected = "4:55 PM"
        message = 'Calling "add_time()" with parameters "1:30 PM", "3:25" should return "4:55 PM"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_period_different(self):
        actual = add_time("5:40 AM", "8:15")
        expected = "1:55 PM"
        message = 'Calling "add_time()" with parameters "5:40 AM", "8:15" should return "1:55 PM"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_nextDay(self):
        actual = add_time("10:15 PM", "11:35")
        expected = "9:50 AM (next day)"
        message = 'Calling "add_time()" with parameters "10:15 PM", "11:35" should return "9:50 AM (next day)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_period_change(self):
        actual = add_time("11:55 AM", "0:10")
        expected = "12:05 PM"
        message = 'The period should change from AM to PM at 12:00'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_twenty_four(self):
        actual = add_time("5:46 AM", "24:00")
        expected = "5:46 AM (next day)"
        message = 'Calling "add_time()" with parameters "5:46 AM", "24:00" should return "5:46 AM (next day)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_multipleDays(self):
        actual = add_time("10:48 PM", "25:15")
        expected = "12:03 AM (2 days later)"
        message = 'Calling "add_time()" with parameters "10:48 PM", "48:12" should return "12:03 AM (2 days later)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_tooManyDays(self):
        actual = add_time("6:25 PM", "536:48")
        expected = "3:13 AM (23 days later)"
        message = 'Calling "add_time()" with parameters "6:25 PM", "536:48" should return "3:13 AM (23 days later)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_no_change(self):
        actual = add_time("10:12 AM", "0:00")
        expected = "10:12 AM"
        message = 'Adding "0:00" should return the initial time "10:12 AM"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_timeChange_sameDay_samePeriod(self):
        actual = add_time("1:30 PM", "4:12", "Saturday")
        expected = "5:42 PM, Saturday"
        message = 'Calling "add_time()" with parameters "1:30 PM", "4:12", "Saturday" should return "5:42 PM, Saturday"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_dayChange(self):
        actual = add_time("10:59 AM", "24:01", "Sunday")
        expected = "11:00 AM, Monday (next day)"
        message = 'Calling "add_time()" with parameters "10:59 AM", "24:01", "Sunday" should return "11:00 AM, Monday (next day)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_multiDays_later(self):
        actual = add_time("11:50 PM", "24:20", "Friday")
        expected = "12:10 AM, Sunday (2 days later)"
        message = 'Calling "add_time()" with parameters "11:50 PM", "24:20", "Friday" should return "12:10 AM, Sunday (2 days later)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)

    def test_tooManyDays_withDay(self):
        actual = add_time("6:25 PM", "536:48", "tuesday")
        expected = "3:13 AM, Thursday (23 days later)"
        message = 'Calling "add_time()" with parameters "6:25 PM", "536:48", "tuesday" should return "3:13 AM, Thursday (23 days later)"'
        try:
            self.assertEqual(actual, expected, message)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    unittest.main()
