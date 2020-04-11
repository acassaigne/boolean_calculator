import unittest


def boolean_calculator(input_boolean):
    if input_boolean == "NOT" + " " + "TRUE":
        return False
    if input_boolean == "FALSE":
        return False
    return True


class TestBooleanCalculatorShould(unittest.TestCase):

    def test_return_true_for_true(self):
        self.assertEqual(True, boolean_calculator("TRUE"))

    def test_return_false_for_false(self):
        self.assertEqual(False, boolean_calculator("FALSE"))

    def test_return_false_for_not_true(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE"))