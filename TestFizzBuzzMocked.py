import unittest
import pymock
import FizzBuzz
"""
Q5. Write the psuedocode for the test_repport method, such that it uses PyMock
mock objects to test the report method of FizzBuzz. [5 pts]
Ans:-

def test_report(self):
#mock the file handle
mock_opener = self.mock()
mock_file = self.mock()
self.expectAndReturn(mock_opener.open('c:/temp/fizzbuzz_report.txt', 'w'), mock_file)
mock_file.write("3 fizz \n")
mock_file.close()

#replay
self.replay()

#call API
self.fb.report(numbers, opener=mock_opener.open)

# verify
self.verify()





"""
class TestFizzBuzzMocked(pymock.PyMockTestCase):
        
    def setUp(self):
        super(TestFizzBuzzMocked, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setUp TestFizzBuzzMocked"

    def tearDown(self):
        super(TestFizzBuzzMocked, self).tearDown()
        self.fb = None

    def test_report(self):
         #mock the file handle
        mock_opener = self.mock()
        mock_file = self.mock()
        self.expectAndReturn(mock_opener.open('c:/temp/fizzbuzz_report.txt', 'w'), mock_file)
        mock_file.write("3 fizz \n")
        mock_file.close()

        #replay
        self.replay()

        #call API
        self.fb.report(numbers, opener=mock_opener.open)

        # verify
        self.verify()

















        


if __name__ == "__main__":
    unittest.main()