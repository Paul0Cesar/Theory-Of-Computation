"""
This file is responsible to test MTND  

This file simplifies your MTND test, you only need to change
the function import below this comment and the call_test

Author: Paulo César
Created At: March 9, 2023
"""

import unittest
from index import start  # CHANGE THIS FOR TEST


def call_test(states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges, start_state, end_state_list, words): return start(
    states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges, start_state, end_state_list, words)  # CHANGE THIS FOR TEST


class Test(unittest.TestCase):

    def test_1(self):
        """
        Default Test
        """
        states = ["0", "1", "2", "3", "4"]
        alphabet = ["a", "b"]
        tape_alphabet = ["A", "B", "*"]
        tape_left_limit = "<"
        blank_symbol = "*"
        edges = [('0', 'a', '1', 'A', 'D'), ('1', 'a', '1', 'a', 'D'), ('1', 'B', '1', 'B', 'D'),
                 ('1', 'b', '2', 'B', 'E'), ('2', 'B', '2',
                                             'B', 'E'), ('2', 'a', '2', 'a', 'E'),
                 ('2', 'A', '0', 'A', 'D'), ('0', 'B', '3',
                                             'B', 'D'), ('3', 'B', '3', 'B', 'D'),
                 ('3', '*', '4', '*', 'E')]
        start_state = "0"
        end_state_list = ['4']
        words = ['*', 'ab', 'ba', 'abb', 'aab', 'aabb']

        expected = ["N", "S", "N", "N", "N", "S"]

        result = call_test(states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, f"Should be :{expected}")

    def test_2(self):
        """
        b*ab*+c*ac*
        """
        states = ["e1", "e2", "e3", "e4", "e5", "e6"]
        alphabet = ["a", "b"]
        tape_alphabet = ["a", "b", "c", "*", "<"]
        tape_left_limit = "<"
        blank_symbol = "*"
        edges = [('e1', 'c', 'e1', 'c', 'D'), ('e1', 'b', 'e1', 'b', 'D'), ('e1', 'a', 'e2', 'b', 'D'), ('e2', 'b', 'e2', 'b', 'D'),
                 ('e2', '*', 'e3', '*', 'E'), ('e3', 'b', 'e3', 'b',
                                               'E'), ('e3', '<', 'e6', '<', 'D'), ('e1', 'a', 'e4', 'c', 'D'),
                 ('e4', 'c', 'e4', 'c', 'D'), ('e4', '*', 'e5', '*', 'E'), ('e5', 'c', 'e5', 'c', 'E'), ('e5', '<', 'e6', '<', 'E')]
        start_state = "e1"
        end_state_list = ['e6']
        words = ['*','bbabb','bbbb','abab','ccacc',"ccccac"]

        expected = ["N", "S", "N", "N", "S", "S"]

        result = call_test(states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, f"Should be :{expected}")


if __name__ == '__main__':
    unittest.main()
