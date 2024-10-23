"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch
from src.functions import greet_name_age, \
                            math_operation,\
                            prompt_name_greeting



#1    2            3          4          
#test_functionname_condition_expected 


class TestFunctions(unittest.TestCase):
    def test_greet_name_age_valid_arguments_expected_string(self):
        #Arrange
        name = "Mark"
        age = 30 
        expected = "Hello Mark, you are 30 years old!"

        #Act
        actual = greet_name_age(name, age)

        #Assert
        self.assertEqual(expected, actual)

    def test_math_operation_addition_returns_sum(self):
        # Arrange
        operand1 = 10
        operand2 = 5
        operation = "+"

        expected = 15.0

        # Act
        actual = math_operation(operand1, operand2, operation)
        
        # Assert
        self.assertEqual(expected, actual)

        # This is another way to do all Arrange, act and assert in a single line of code

        # self.assertEqual(15.0, math_operation (10, 5, "+"))

    def test_math_operation_subtraction_returns_difference(self):
        # Arrange
        operand1 = 10
        operand2 = 5
        operation = "-"

        expected = 5.0

        # Act
        actual = math_operation(operand1, operand2, operation)
        
        # Assert
        self.assertEqual(expected, actual)

        # This is another way to do all Arrange, act and assert in a single line of code

        # self.assertEqual(5.0, math_operation (10, 5, "-"))

    def test_math_operation_invalid_operator_valueerror(self):
        # Arrange
        operator1 = 4
        operator2 = 15

        # use an invalid operator
        operation = "*"
        expected = "Invalid operation."


        # Act and Assert
        with self.assertRaises(ValueError) as context: 
            math_operation(operator1, operator2, operation)
        
        self.assertEqual(expected, str(context.exception))

    def test_prompt_name_greeting_valid_inputs_greeting_returned(self):
        #builtins.input: allows us to mock input behaviour


        with patch ("builtins.input") as mock_input:
            # Arrange
            mock_input.side_effect = ["Mark," "Winnipeg"]
            expected = "Your name is Mark and your currenty city is Winnipeg"

            # Act
            actual = prompt_name_greeting()

        # Assert
        self.assertEqual(expected, actual)

