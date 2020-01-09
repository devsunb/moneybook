from datetime import datetime

from openpyxl import load_workbook, Workbook

from moneybook.util import comma_str_to_int


class Excel:
    def __init__(self):
        self.wb = None
        self.ws = None

    def new(self):
        self.wb = Workbook()
        self.ws = self.wb.active

    def open(self, path):
        self.wb = load_workbook(path)
        self.ws = self.wb.active

    def select_ws(self, name):
        self.ws = self.wb[name]

    def create_ws(self, name, index=None):
        self.ws = self.wb.create_sheet(name, index)

    def get_data(self, min_row=None, max_row=None, min_col=None, max_col=None):
        return [[datetime.strptime(r[0].value, '%Y.%m.%d %H:%M:%S'), r[1].value, comma_str_to_int(r[2].value),
                 comma_str_to_int(r[3].value), r[4].value, r[5].value, r[6].value]
                for r in self.ws.iter_rows(min_row, max_row, min_col, max_col)]
