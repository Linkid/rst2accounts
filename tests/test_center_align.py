#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from rst2accounts.main import center_align


class TestCenterAlign(unittest.TestCase):
    def test_float_in_odd_cell(self):
        # one digit
        cell = ' ' * 7
        centered_digit_1 = center_align(cell, '1')
        expected_str_1 = '   1   '
        self.assertEqual(len(expected_str_1), 7)
        self.assertEqual(centered_digit_1, expected_str_1)

        # two digits
        centered_digit_2 = center_align(cell, '21')
        expected_str_21 = '  21   '
        self.assertEqual(len(expected_str_21), 7)
        self.assertEqual(expected_str_1.index('1'), expected_str_21.index('1'))
        self.assertEqual(centered_digit_2, expected_str_21)

        # one decimal
        centered_float_1 = center_align(cell, '1.0', 1)
        expected_str_10 = '   1.0 '
        self.assertEqual(len(expected_str_10), 7)
        self.assertEqual(expected_str_1.index('1'), expected_str_10.index('1'))
        self.assertEqual(centered_float_1, expected_str_10)

        # two decimals
        centered_float_2 = center_align(cell, '1.00', 1)
        expected_str_100 = '   1.00'
        self.assertEqual(len(expected_str_100), 7)
        self.assertEqual(expected_str_1.index('1'), expected_str_100.index('1'))
        self.assertEqual(centered_float_2, expected_str_100)

        # two decimals and two decimals
        centered_float_3 = center_align(cell, '21.00', 1)
        expected_str_2100 = '  21.00'
        self.assertEqual(len(expected_str_2100), 7)
        self.assertEqual(expected_str_1.index('1'), expected_str_2100.index('1'))
        self.assertEqual(centered_float_3, expected_str_2100)

    def test_float_in_even_cell(self):
        # one digit
        cell = ' ' * 8
        centered_digit_1 = center_align(cell, '1')
        expected_str_1 = '    1   '
        self.assertEqual(len(expected_str_1), 8)
        self.assertEqual(centered_digit_1, expected_str_1)

        # two digits
        centered_digit_2 = center_align(cell, '21')
        expected_str_21 = '   21   '
        self.assertEqual(len(expected_str_21), 8)
        self.assertEqual(expected_str_1.index('1'), expected_str_21.index('1'))
        self.assertEqual(centered_digit_2, expected_str_21)

        # one decimal
        centered_float_1 = center_align(cell, '1.0', 1)
        expected_str_10 = '    1.0 '
        self.assertEqual(len(expected_str_10), 8)
        self.assertEqual(expected_str_1.index('1'), expected_str_10.index('1'))
        self.assertEqual(centered_float_1, expected_str_10)

        # two decimals
        centered_float_2 = center_align(cell, '1.00', 1)
        expected_str_100 = '    1.00'
        self.assertEqual(len(expected_str_100), 8)
        self.assertEqual(expected_str_1.index('1'), expected_str_100.index('1'))
        self.assertEqual(centered_float_2, expected_str_100)

        # two decimals and two decimals
        centered_float_3 = center_align(cell, '21.00', 1)
        expected_str_2100 = '   21.00'
        self.assertEqual(len(expected_str_2100), 8)
        self.assertEqual(expected_str_1.index('1'), expected_str_2100.index('1'))
        self.assertEqual(centered_float_3, expected_str_2100)

if __name__ == '__main__':
    unittest.main()
