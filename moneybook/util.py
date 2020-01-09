import xml.etree.ElementTree as elemTree
from datetime import datetime


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.term = 0

    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()
        self.term = (self.end_time - self.start_time).seconds


def comma_str_to_int(s):
    return int(s.replace(',', ''))


def xml_tree(data):
    return elemTree.fromstring(data)
