import unittest

from moneybook.moneybook import Moneybook


class TestMoneybook(unittest.TestCase):
    def setUp(self):
        self.m = Moneybook('http://192.168.137.94:8888/')

    def test_get_init_data(self):
        print(self.m.get_init_data())

    def test_get_data_by_period(self):
        print(self.m.get_data_by_period())


if __name__ == '__main__':
    unittest.main()
