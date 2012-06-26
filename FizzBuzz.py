"""
Q1. Why is the report method untestable ? [2 pts]
--> report_file open and path is an external collaborative (platform and system environment dependent) which is handled in the function. hence,  it is untestable.


Q2. How will you change the api of the report method to make it more testable ? [2 pts]



"""



class FizzBuzz(object):
    def report(self, numbers, file_handle):
        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                    msg += "buzz "
                    fizzbuzz_found = True
            if fizzbuzz_found:
                        file_handle.write(msg + "\n")

            


if "__main__" == __name__:
        fb = FizzBuzz()
        file_handle = open('temp.txt', 'w') # can create open wrapper
        fb.report(range(100), file_handle)
        file_handle.close()

            
