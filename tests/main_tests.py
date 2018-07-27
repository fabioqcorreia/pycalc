"""
Testes principais e unitários
"""

import unittest
from utils.utilities import SUM_PARAM_A, SUM_PARAM_B, SUB_PARAM_A, SUB_PARAM_B
from sum.summation import Summatory
from sub.subtract import Subtraction


class TestCalcing(unittest.TestCase):

    def test_sum(self):
        summatory = Summatory()
        sum_result = summatory.add(SUM_PARAM_A, SUM_PARAM_B)
        self.assertEqual(3, sum_result)

    def test_sub(self):
        subtraction = Subtraction()
        sub_result = subtraction.remove(SUB_PARAM_A, SUB_PARAM_B)
        self.assertEqual(1, sub_result)


if __name__ == '__main__':
    unittest.main()
