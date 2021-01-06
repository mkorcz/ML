import unittest
import machineLearning


class TestReadCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def test_read(self):
        self.assertIsNotNone(machineLearning.readCSV('exportDataframe.csv'))
