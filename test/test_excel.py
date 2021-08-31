import os
import random
import unittest
import numpy as np
from moneybook.excel import Excel


class TestExcel(unittest.TestCase):
    def test_save_and_open_with_first_cell(self):
        test_file_path = 'test1.xlsx'
        test_ws_name = 'test_ws'
        test_value = 'test_value'
        e = Excel(test_file_path)
        e.create_ws(test_ws_name)
        e.select_ws(test_ws_name)
        e.set_value(1, 1, test_value)
        e.save()
        e.open(test_file_path)
        e.select_ws(test_ws_name)
        v = e.get_value(1, 1)
        self.assertEqual(test_value, v)
        os.remove(test_file_path)

    def test_save_and_open_with_10x10_cells(self):
        test_file_name = 'test2.xlsx'
        test_ws_name = 'test_ws'
        test_dtype = np.int32

        test_values = np.random.randint(0, 100, (10, 10), test_dtype)
        e = Excel(test_file_name)
        e.create_ws(test_ws_name)
        e.select_ws(test_ws_name)
        e.set_values(1, 1, test_values)
        e.save()
        e.open(test_file_name)
        e.select_ws(test_ws_name)
        v = e.get_values(1, 1, 10, 10, test_dtype)
        self.assertTrue(np.array_equal(test_values, v))


if __name__ == '__main__':
    unittest.main()
