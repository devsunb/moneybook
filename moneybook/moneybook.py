from datetime import datetime

import requests
from yarl import URL

from moneybook.util import xml_tree


class Moneybook:
    def __init__(self, base_url):
        self.base_url = URL(base_url)

    def get_init_data(self):
        url = self.base_url.with_path('/moneyBook/getInitData')
        return requests.get(url).text

    def get_data_by_period(self):
        query_data = {
            'startDate': datetime(2020, 1, 1).strftime('%Y-%m-%d'),
            'endDate': datetime(2020, 1, 31).strftime('%Y-%m-%d'),
            'mbid': '1',
            'assetId': ''
        }
        url = self.base_url.with_path('/moneyBook/getDataByPeriod').with_query(query_data)
        return self.parse_data_by_period(requests.get(url).text)

    @staticmethod
    def parse_data_by_period(data):
        tree = xml_tree(data)
        parsed = {}
        for r in tree.findall('row'):
            rid = r.find('id').text
            parsed[rid] = {}
            for i in ['mbDate', 'inOutCode', 'assetId', 'payType', 'inOutType', 'mcid', 'mbCategory', 'mcscid',
                      'subCategory', 'mbContent', 'mbDetailContent', 'mbCash']:
                parsed[rid][i] = r.find(i).text
            if '이체' in parsed[rid]['inOutType']:
                parsed[rid]['toAssetId'] = r.find('toAssetId').text
        return parsed
