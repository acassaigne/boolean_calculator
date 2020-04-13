import unittest




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

    def test_return_True_for_not_false(self):
        self.assertEqual(True, boolean_calculator("NOT FALSE"))

    def test_raise_error_for_not_only_expression(self):
        with self.assertRaises(InvalidBooleanExpression):
            boolean_calculator("NOT")

    def test_x(self):
        self.assertEqual(True, boolean_calculator("TRUE AND TRUE"))

    def test_y(self):
            self.assertEqual(False, boolean_calculator("TRUE AND FALSE"))

    def test_z(self):
        self.assertEqual(False, boolean_calculator("FALSE AND TRUE"))


def boolean_calculator(input_boolean):
    if input_boolean.find(" ") != -1:
        index_separator = input_boolean.find(" ")
        var1 = input_boolean[:index_separator]
        rest_input = input_boolean[index_separator+1:]
        index_separator = rest_input.find(" ")
        and_word = rest_input[:index_separator]
        var2 = rest_input[index_separator+1:]
        if input_boolean == var1 + " " + and_word + " " + var2:
            return boolean_calculator(var1) and boolean_calculator(var2)
    if input_boolean[0:3] == "NOT":
        return not boolean_calculator(input_boolean[4:])
    if input_boolean == "FALSE":
        return False
    if input_boolean == "TRUE":
        return True
    if input_boolean == "":
        raise InvalidBooleanExpression

