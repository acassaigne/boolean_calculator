import unittest


def boolean_calculator(input_boolean):
    if input_boolean == "NOT" + " " + "FALSE":
        return True
    if input_boolean == "NOT" + " " + "TRUE":
        return False
    if input_boolean == "FALSE":
        return False
    if input_boolean == "TRUE":
        return True
    if input_boolean == "":
        raise InvalidBooleanExpression


class InvalidBooleanExpression(Exception):
    pass


class TestBooleanCalculatorShould(unittest.TestCase):

    def test_return_true_for_true(self):
        self.assertEqual(True, boolean_calculator("TRUE"))

    def test_return_false_for_false(self):
        self.assertEqual(False, boolean_calculator("FALSE"))

    def test_return_false_for_not_true(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE"))

    def test_raise_error_for_an_empty_boolean_expression(self):
        with self.assertRaises(InvalidBooleanExpression):
            boolean_calculator("")

    def test_x(self):
        self.assertEqual(True, boolean_calculator("NOT FALSE"))