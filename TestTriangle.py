# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_input(self):
        """ Test if the function can handle invalid input """

        # check for invalid value of length
        self.assertEqual(classifyTriangle(-1, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 0, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(3, 2, 3.2), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(3, 2, 6), 'NotATriangle')
        self.assertEqual(classifyTriangle(6, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(201, 201, 201), 'NotATriangle')

        # check for string input
        self.assertEqual(classifyTriangle("a", 2, 3), "InvalidInput")
        self.assertEqual(classifyTriangle(1, "b", 3), "InvalidInput")
        self.assertEqual(classifyTriangle(1, 2, "C"), "InvalidInput")

    def test_result(self):
        """ Test if the function returns the correct result """

        self.assertEqual(classifyTriangle(2, 3, 4), "Scalene")
        self.assertEqual(classifyTriangle(4, 5, 3), "Right")
        self.assertEqual(classifyTriangle(3, 3, 5), "Isoceles")
        self.assertEqual(classifyTriangle(3, 5, 3), "Isoceles")
        self.assertEqual(classifyTriangle(5, 3, 3), "Isoceles")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
