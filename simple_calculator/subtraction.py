# !/usr/bin/python
# coding=UTF-8
# Written by Veeresh Katageri <veeresh.mcisi@gmail.com>, March 2020

"""This script is used to perform Subtraction

- author: Veeresh Katageri
- status: alpha
- e-mail: veeresh.mcisi@gmail.com
"""

import os
import argparse

class Subtraction:

    """Class Subtraction is used to perform Subtraction operation"""

    def __init__(self, number_1, number_2):
        """The init function of the class Subtraction

        :param number_1: is the number_1
        :type number_2: str
        :param number_2: is the name of number_2
        :type number_2: str
        """

        self.number_1 = int(number_1) if number_1.isnumeric() else float(number_1)
        self.number_2 = int(number_2) if number_2.isnumeric() else float(number_2)

    def run(self):
        """ The main function for Class Subtraction."""

        result = self.number_1 - self.number_2
        print("Subtraction of numbers", result)
        return result


def main(number_1="", number_2=""):
    """ This method is required because
        1. it can be called from simple_calculator.py as a submodule
        2. it can be called standalone from command line.
    """

    parser = argparse.ArgumentParser(description="Subtraction")
    parser.add_argument('-n1', '--number_1', type=str, help='A valid 1st number')
    parser.add_argument('-n2', '--number_2', type=str, help='A valid 2nd number')

    print("Subtraction")
    if not number_1.strip() and not number_2.strip():
        args = parser.parse_args()
        if 1:
            print("Script is called directly", os.path.dirname(sys.argv[0]))
            submodule = Subtraction(args.number_1, args.number_2)
            submodule.run()
        else:
            print("Error printing arguments")
    else:
        print("Argument passed from simple_calculator.py")
        print("number_1 %s, number_2  %s" % (number_1, number_2))
        args, unknown = parser.parse_known_args(['--number_1', number_1,
                                                 '--number_2', number_2])
        args.number_1 = number_1
        args.number_2 = number_2

        submodule = Subtraction(args.number_1, args.number_2)
        submodule.run()


if __name__ == '__main__':
    main()