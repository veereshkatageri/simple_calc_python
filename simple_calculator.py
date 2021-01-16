# !/usr/bin/python
# coding=UTF-8
# Written by Veeresh Katageri <veeresh.mcisi@gmail.com>, March 2020

"""This script is used to implement simple 

- author: Veeresh Katageri
- status: alpha
- e-mail: veeresh.mcisi@gmail.com
"""

import os
import sys
import argparse

from simple_calculator import addition
from simple_calculator import subtraction
from simple_calculator import multiplication
from simple_calculator import division

class SimpleCalculator:

    """ Class SimpleCalculator is used to handle the complete logic of Simple Calculator"""

    def __init__(self, number_1, number_2, operator):
        """The init function of the class SimpleCalculator

        :param number_1: is the number_1
        :type number_2: str
        :param number_2: is the name of number_2
        :type number_2: str
        :param operator: is the operator
        :type operator: str
        """

        self.number_1 = number_1
        self.number_2 = number_2
        self.operator = operator

    def perform_operation(self):
        """This method performs operation."""
        if self.operator == '+':
            print("Perform addition")
            addition.main(self.number_1, self.number_2)
        elif self.operator == '-':
            print("Perform subtraction")
            subtraction.main(self.number_1, self.number_2)
        elif self.operator == '*':
            print("Perform multiplication")
            multiplication.main(self.number_1, self.number_2)
        elif self.operator == '/':
            print("Perform division")
            division.main(self.number_1, self.number_2)
        else:
            print("Invalid operator")

    def run(self):
        """ The main function for SimpleCalculator."""

        try:
            if (self.number_1.isnumeric() and self.number_2.isnumeric() or
               (float(self.number_1) or float(self.number_2))):
                self.perform_operation()
        except:
            print("One of the argument is not valid numeric")

PARSER = argparse.ArgumentParser(description="Simple Calculator")
PARSER.add_argument('-n1', '--number_1', type=str, help='A valid 1st number')
PARSER.add_argument('-n2', '--number_2', type=str, help='A valid 2nd number')
PARSER.add_argument('-op', '--operator', type=str, help='A valid operator')
ARGS = PARSER.parse_args()

if __name__ == '__main__':
    print("Simple Calculator")
    APP = SimpleCalculator(ARGS.number_1, ARGS.number_2, ARGS.operator)
    APP.run()

