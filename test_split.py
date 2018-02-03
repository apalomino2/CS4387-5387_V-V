# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:11:00 2018

@author: Abnermal
"""

import unittest
from split import split

class TestSplit(unittest.TestCase):
    def test_1(self):
        expected = ["c", "s"]
        actual = split("cs", 1)
        self.assertListEqual(expected, actual)

    def test_2(self):
        with self.assertRaises(TypeError):
            actual = split(None, 2)

    def test_3(self):
        expected = ["cs rocks"]
        actual = split("cs rocks", 8)
        self.assertListEqual(expected, actual)

    def test_4(self):
        expected = ["cs"]
        actual = split("cs", 5)
        self.assertListEqual(expected, actual)

    def test_5(self):
        with self.assertRaises(ValueError):
            actual = split("cs", -1)

    def test_6(self):
        with self.assertRaises(ValueError):
            actual = split("cs", 0)

    def test_7(self):
        with self.assertRaises(ValueError):
            actual = split("", 0)

    def test_8(self):
        expected = ["$"]
        actual = split("$", 1)
        self.assertListEqual(expected, actual)

    def test_9(self):
        expected = ["a", "b", "c", "$"]
        actual = split("abc$", 1)
        self.assertListEqual(expected, actual)

    def test_10(self):
        expected = ["+"]
        actual = split("+", 1)
        self.assertListEqual(expected, actual)

    def test_11(self):
        expected = ["-"]
        actual = split("-", 1)
        self.assertListEqual(expected, actual)

    def test_12(self):
        expected = ["/"]
        actual = split("/", 1)
        self.assertListEqual(expected, actual)

    def test_13(self):
        expected = ["*"]
        actual = split("*", 1)
        self.assertListEqual(expected, actual)

    def test_14(self):
        expected = ["!"]
        actual = split("!", 1)
        self.assertListEqual(expected, actual)

    def test_15(self):
        expected = ["+", "+"]
        actual = split("++", 1)
        self.assertListEqual(expected, actual)

    def test_16(self):
        expected = ["-", "-"]
        actual = split("--", 1)
        self.assertListEqual(expected, actual)

    def test_17(self):
        expected = ["\n"]
        actual = split("\n", 2)
        self.assertListEqual(expected, actual)

    def test_18(self):
        expected = ["\t"]
        actual = split("\t", 3)
        self.assertListEqual(expected, actual)

    def test_19(self):
        expected = ["\\"]
        actual = split("\\", 4)
        self.assertListEqual(expected, actual)

    def test_20(self):
        expected = ["\r"]
        actual = split("\r", 5)
        self.assertListEqual(expected, actual)

    def test_21(self):
        expected = [""]
        actual = split("", 3)
        self.assertListEqual(expected, actual)

    def test_22(self):
        expected = ["cs"]
        actual = split("cs", 2147483647)
        self.assertListEqual(expected, actual)

    def test_23(self):
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
