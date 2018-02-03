# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:11:00 2018

@author: Abnermal
"""

import unittest
from split import split

class TestSplit(unittest.TestCase):
    def test_1(self):
        """
        @Test a simple base case to show the program can handle a simple input
        """
        expected = ["c", "s"]
        actual = split("cs", 1)
        self.assertListEqual(expected, actual)

    def test_2(self):
        """
        @Test the handling of a null string
        """
        with self.assertRaises(TypeError):
            actual = split(None, 2)

    def test_3(self):
        """
        @Test how the method functions when given a string and a size 
        that matches the size of that string
        """
        expected = ["cs rocks"]
        actual = split("cs rocks", 8)
        self.assertListEqual(expected, actual)

    def test_4(self):
        """
        @Test how the method functions when given a string and a size 
        that is greater than the size of that string
        """
        expected = ["cs"]
        actual = split("cs", 5)
        self.assertListEqual(expected, actual)

    def test_5(self):
        """
        @Test how the method handles a negative as the size. Since a string 
        cannot have negative size, it should raise an error.
        """
        with self.assertRaises(ValueError):
            actual = split("cs", -1)

    def test_6(self):
        """
        @Test how the method handles zero as the size. Since the string could 
        be composed of an infinite number of emtpy strings, it should raise an 
        error.
        """
        with self.assertRaises(ValueError):
            actual = split("cs", 0)

    def test_7(self):
        """
        @Test how the method handles an emtpy string and zero as the size.
        """
        with self.assertRaises(ValueError):
            actual = split("", 0)

    def test_8(self):
        """
        @Test how the method handles a special character.
        """
        expected = ["$"]
        actual = split("$", 1)
        self.assertListEqual(expected, actual)

    def test_9(self):
        """
        @Test how the method handles a special character after a string.
        """
        expected = ["a", "b", "c", "$"]
        actual = split("abc$", 1)
        self.assertListEqual(expected, actual)

    def test_10(self):
        """
        @Test how the method handles a math operation in the string.
        """
        expected = ["+"]
        actual = split("+", 1)
        self.assertListEqual(expected, actual)

    def test_11(self):
        """
        @Test how the method handles a math operation in the string.
        """
        expected = ["-"]
        actual = split("-", 1)
        self.assertListEqual(expected, actual)

    def test_12(self):
        """
        @Test how the method handles a math operation in the string.
        """
        expected = ["/"]
        actual = split("/", 1)
        self.assertListEqual(expected, actual)

    def test_13(self):
        """
        @Test how the method handles a math operation in the string.
        """
        expected = ["*"]
        actual = split("*", 1)
        self.assertListEqual(expected, actual)

    def test_14(self):
        """
        @Test how the method handles a logical operation in the string.
        """
        expected = ["!"]
        actual = split("!", 1)
        self.assertListEqual(expected, actual)

    def test_15(self):
        """
        @Test how the method handles a math operation in the string. This 
        characters are special because the represent an operation in many 
        programming languages.
        """
        expected = ["+", "+"]
        actual = split("++", 1)
        self.assertListEqual(expected, actual)

    def test_16(self):
        """
        @Test how the method handles a math operation in the string. This 
        characters are special because the represent an operation in many 
        programming languages.
        """
        expected = ["-", "-"]
        actual = split("--", 1)
        self.assertListEqual(expected, actual)

    def test_17(self):
        """
        @Test an escape character. We assume these two characters should be 
        treated as one.
        """
        expected = ["\n"]
        actual = split("\n", 2)
        self.assertListEqual(expected, actual)

    def test_18(self):
        """
        @Test an escape character. We assume these two characters should be 
        treated as one.
        """
        expected = ["\t"]
        actual = split("\t", 3)
        self.assertListEqual(expected, actual)

    def test_19(self):
        """
        @Test an escape character. We assume these two characters should be 
        treated as one.
        """
        expected = ["\\"]
        actual = split("\\", 4)
        self.assertListEqual(expected, actual)

    def test_20(self):
        """
        @Test an escape character. We assume these two characters should be 
        treated as one.
        """
        expected = ["\r"]
        actual = split("\r", 5)
        self.assertListEqual(expected, actual)

    def test_21(self):
        """
        @Test how the method handles an emtpy string.
        """
        expected = [""]
        actual = split("", 3)
        self.assertListEqual(expected, actual)

    def test_22(self):
        """
        @Test the maximum for an integer.
        """
        expected = ["cs"]
        actual = split("cs", 2147483647)
        self.assertListEqual(expected, actual)

    def test_23(self):
        """
        @Test the minimum for an integer.
        """
        with self.assertRaises(ValueError):
            actual = split("cs", -2147483648)

"""
    Test 24:
    Actual: \b
    Expected: "\b"
    Size: 1

    Test 25:
    Actual: /**
    Expected: "/**"
    Size: 1

    Test 26:
    Actual: **/
    Expected: "**/"
    Size: 1

    Test 27:
    Actual: String
    Excpected: Exceptoin TypeError
    Size: String

    Test 28:
    Actual: (Int Value)
    Expected: Exception TypeError
    Size: 1

    def test_extra(self):
        expected =
        actual =
        self.assertListEqual(expected, actual)
"""

if __name__ == '__main__':
    unittest.main()
