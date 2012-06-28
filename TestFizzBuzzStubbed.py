import unittest
import pymock
import FizzBuzz
"""
Q3. What will be printed when we execute 'python FizzBuzzStubbed.py' ? [3 pts]

Ans:-

setUpClass FizzBuzzStubbed
setup
test_report
teardown
test_report
setup
test_report
teardown
tearDownClass









Q4. Implement MyStub class so that you can send it as a fake object to the
report method of FizzBuzz object from a test case. [3 pts]
Ans:-

###############myStub Class############################
class MyStub(object):

def gen_open_stub(output_stub):
def open(fpath, mode):
return output_stub
return open

def __init__(self):
self.values = []
self.cnt = 0
def write(self, value):
self.values.append(value)
def close(self):
self.closed = True
def readline(self):
if self.cnt <= len(self.values):
ret_val = self.values[self.cnt]
self.cnt += 1
return ret_val
else:
raise StopError()
############# And appropriate changes required for test_report method ##########################


def test_report(self):
print "test_report"
output_stub = MyStub()
my_open= MyStub.gen_open_stub(output_stub)
fb = FizzBuzz.FizzBuzz()
fb.report([33], my_open)
self.assertEqual(output_stub.readline(), '33 fizz \n' )
fb.report([55], my_open)
self.assertEqual(output_stub.readline(), '55 buzz \n' )
fb.report([15], my_open)
self.assertEqual(output_stub.readline(), '15 fizz buzz \n' )
pass

"""
class MyStub(object):
    pass








    
class TestFizzBuzzStubbed(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        print "setUpClass FizzBuzzStubbed"
        
    def setUp(self):
        super(TestFizzBuzzStubbed, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setup"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        
    def tearDown(self):
        super(TestFizzBuzzStubbed, self).tearDown()
        self.fb = None
        print "teardown"

    def test_report(self):
        print "test_report"
        pass

    def test_report_for_empty_list(self):
        print "test_report"
        pass

if __name__ == "__main__":
    unittest.main()