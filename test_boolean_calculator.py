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

    def test_return_true_for_true_and_true(self):
        self.assertEqual(True, boolean_calculator("TRUE AND TRUE"))

    def test_return_false_for_true_and_false(self):
            self.assertEqual(False, boolean_calculator("TRUE AND FALSE"))

    def test_return_false_for_false_and_true(self):
        self.assertEqual(False, boolean_calculator("FALSE AND TRUE"))

    def test_raise_error_for_and_only_operator_without_operand(self):
        with self.assertRaises(InvalidBooleanExpression):
            boolean_calculator("AND")

    def test_raise_error_for_and_operator_with_only_one_operand(self):
        with self.assertRaises(InvalidBooleanExpression):
            boolean_calculator("TRUE AND")

    def test_return_false_for_true_and_true_and_false(self):
        self.assertEqual(False, boolean_calculator("TRUE AND TRUE AND FALSE"))

    def test_return_true_for_true_or_false(self):
        self.assertEqual(True, boolean_calculator("TRUE OR TRUE"))

    def test_return_true_for_and_precedent_or(self):
        self.assertEqual(True, boolean_calculator("FALSE AND TRUE OR TRUE"))

    def test_y(self):
        self.assertEqual(True, boolean_calculator("NOT FALSE OR TRUE"))


def has_separator(string):
    return string.find(" ") != -1


def extract_first_word_from(string):
    if has_separator(string):
        index_separator = string.find(" ")
        first_word = string[:index_separator]
        return first_word, string[index_separator + 1:]
    return string, ""


def _boolean_to_string(boolean):
    return str(boolean).upper()


def atom_to_boolean(string_boolean):
    if string_boolean == "FALSE":
        return False
    if string_boolean == "TRUE":
        return True
    raise InvalidBooleanExpression


def boolean_calculator(boolean_expression):
    first_word, rest_expression = extract_first_word_from(boolean_expression)
    if rest_expression == "":
        return atom_to_boolean(first_word)

    second_word, rest_expression = extract_first_word_from(rest_expression)
    if first_word == "NOT":
        result = not boolean_calculator(second_word)
        return boolean_calculator(_boolean_to_string(result) + " " + rest_expression)

    if second_word not in ["AND", "OR"]:
        raise InvalidBooleanExpression

    third_word, rest_expression = extract_first_word_from(rest_expression)
    if second_word == "AND":
        result = boolean_calculator(first_word) and boolean_calculator(third_word)
        return boolean_calculator(_boolean_to_string(result) + " " + rest_expression)
    if second_word == "OR":
        result = boolean_calculator(first_word) or boolean_calculator(third_word)
        return boolean_calculator(_boolean_to_string(result) + " " + rest_expression)



