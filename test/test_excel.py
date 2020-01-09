import unittest
from datetime import datetime

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from moneybook.excel import Excel


class TestExcel(unittest.TestCase):
    def setUp(self):
        self.e = Excel()

    def test_open(self):
        self.e.open('data\\test.xlsx')
        self.assertIsInstance(self.e.wb, Workbook)
        self.assertIsInstance(self.e.ws, Worksheet)

    def test_get_data(self):
        self.e.open('data\\test.xlsx')
        data = self.e.get_data(12, None, 2, 8)
        expect = [[datetime(2019, 11, 11, 10, 28, 22), '입금', 400000, 502038, '0032', '세이프박스', '']]
        self.assertListEqual(data, expect)


if __name__ == '__main__':
    unittest.main()
