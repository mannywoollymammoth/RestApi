import unittest
from unittest.mock import patch
from CommandLineInterface import CommandLineInterface


class TestCommandLineInterface(unittest.TestCase):
    def test_prompt(self):
        user_input = ['data1.csv', 'q']
        expected_output = ['data1.csv']

        with patch('builtins.input', side_effect=user_input):
            result = CommandLineInterface().prompt()
        self.assertEqual(result, expected_output)

    def test_prompt2(self):
        user_input = ['data1.csv', 'data2.csv', 'data3.csv', 'q']
        expected_output = ['data1.csv', 'data2.csv', 'data3.csv']

        with patch('builtins.input', side_effect=user_input):
            result = CommandLineInterface().prompt()
        self.assertEqual(result, expected_output)

    def test_prompt3(self):
        user_input = ['q']
        expected_output = []

        with patch('builtins.input', side_effect=user_input):
            result = CommandLineInterface().prompt()
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
