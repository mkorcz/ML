import unittest

import dataCollecting
from dataCollecting import validateLinks

class TestVaidateLinks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def test_validateData(self):
        correctTable = ['https://www.skiresort.info/ski-resort/bialka-tatrzanska-kotelnicakaniowkabania/test-report/', 'https://www.skiresort.info/ski-resort/szczyrk-mountain-resort/test-result/size/']
        self.assertIsNotNone(dataCollecting.validateLinks(correctTable))

