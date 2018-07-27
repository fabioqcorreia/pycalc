"""
Calculadora teste para execução de cobertura e treino de testes unitários com TDD.
"""

from sum.summation import Summatory
from sub.subtract import Subtraction

class Calculator:

    def execute_sum(self):

        summatory = Summatory()

        print(str(summatory.add(2, 3)))

    def execute_sub(self):

        subtraction = Subtraction()

        print(str(subtraction.remove(2, 3)))


calculator = Calculator()

calculator.execute_sum()
calculator.execute_sub()