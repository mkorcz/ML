import unittest
import dataCollecting



class TestDataCollecting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_validateData(self):
        self.assertIsNot(dataCollecting.validateLinks(['https://www.skiresort.info/ski-resort/szczyrk-mountain-resort/test-result/size/','https://www.skiresort.info/ski-resort/szczyrk-mountain-resort/test-result/size/']), [])


    def test_makeDF(self):
        self.assertIsNot(dataCollecting.makeDF([['36.6', '733', '9'], ['18.3', '230', '19'], ['4', '261', '2']], ['Routes total', 'Elevation difference', 'Lifts total']), [])

    def test_appendingAreasName(self):
        self.assertIsNotNone(self)

class TestValidateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

   # def test_validateData(self):
    #    self.assertIsNotNone(dataCollecting.validateLinks(self))


if __name__ == '__main__':
    unittest.main()