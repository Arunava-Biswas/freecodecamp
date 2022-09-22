import unittest
import shape_calculator


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.rect = shape_calculator.Rectangle(3, 6)
        self.sq = shape_calculator.Square(5)

    def test_subclass(self):
        actual = issubclass(shape_calculator.Square, shape_calculator.Rectangle)
        expected = True
        message = 'Expected Square class to be a subclass of the Rectangle class.'
        self.assertEqual(actual, expected, message)

    def test_distinct_classes(self):
        actual = shape_calculator.Square is not shape_calculator.Rectangle
        expected = True
        message = 'Expected Square class to be a distinct class from the Rectangle class.'
        self.assertEqual(actual, expected, message)

    def test_square_is_square_and_rectangle(self):
        actual = isinstance(self.sq, shape_calculator.Square) and isinstance(self.sq, shape_calculator.Square)
        expected = True
        message = 'Expected square object to be an instance of the Square class and the Rectangle class.'
        self.assertEqual(actual, expected, message)

    def test_rectangle_string(self):
        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        message = 'Expected string representation of rectangle to be "Rectangle(width=3, height=6)"'
        self.assertEqual(actual, expected, message)

    def test_square_string(self):
        actual = str(self.sq)
        expected = "Square(side=5)"
        message = 'Expected string representation of square to be "Square(side=5)"'
        self.assertEqual(actual, expected, message)

    def test_area(self):
        actual = self.rect.get_area()
        expected = 18
        message1 = 'Expected area of rectangle to be 18'
        self.assertEqual(actual, expected, message1)
        actual = self.sq.get_area()
        expected = 25
        message2 = 'Expected area of rectangle to be 25'
        self.assertEqual(actual, expected, message2)

    def test_perimeter(self):
        actual = self.rect.get_perimeter()
        expected = 18
        message1 = 'Expected perimeter of rectangle to be 18'
        self.assertEqual(actual, expected, message1)
        actual = self.sq.get_perimeter()
        expected = 20
        message2 = 'Expected perimeter of rectangle to be 20'
        self.assertEqual(actual, expected, message2)

    def test_diagonal(self):
        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        message1 = 'Expected diagonal of rectangle to be 6.708203932499369'
        self.assertEqual(actual, expected, message1)
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        message2 = 'Expected diagonal of rectangle to be 7.0710678118654755'
        self.assertEqual(actual, expected, message2)

    def test_set_atributes(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        message1 = 'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"'
        self.assertEqual(actual, expected, message1)
        actual = str(self.sq)
        expected = "Square(side=2)"
        message2 = 'Expected string representation of square after setting new values to be "Square(side=2)"'
        self.assertEqual(actual, expected, message2)
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        message3 = 'Expected string representation of square after setting width to be "Square(side=4)"'
        self.assertEqual(actual, expected, message3)

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        message = 'Expected rectangle picture to be different.'
        self.assertEqual(actual, expected, message)

    def test_squaree_picture(self):
        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        message = 'Expected square picture to be different.'
        self.assertEqual(actual, expected, message)

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture."
        message = 'Expected message: "Too big for picture."'
        self.assertEqual(actual, expected, message)

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        actual = self.rect.get_amount_inside(self.sq)
        expected = 6
        message = 'Expected `get_amount_inside` to return 6.'
        self.assertEqual(actual, expected, message)

    def test_get_amount_inside_two_rectangles(self):
        rect2 = shape_calculator.Rectangle(4, 8)
        actual = rect2.get_amount_inside(self.rect)
        expected = 1
        message = 'Expected `get_amount_inside` to return 1.'
        self.assertEqual(actual, expected, message)

    def test_get_amount_inside_none(self):
        rect2 = shape_calculator.Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        message = 'Expected `get_amount_inside` to return 0.'
        self.assertEqual(actual, expected, message)


if __name__ == "__main__":
    unittest.main()
