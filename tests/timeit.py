import time
import unittest
from decorators import timeit

def sum_function(n):
    '''Function to be timed in some of the below tests'''
    total = 0
    for x in list(range(n+1)):
        total += x

    return total

class TestTimeit(unittest.TestCase):

    def test_return_values(self):
        '''Test that the return values of the timed function are correct'''
        
        math_sum = lambda n: (n*(n+1))/2

        @timeit()
        def timed_sum(n):
            return sum_function(n)

        nums = (10**i for i in range(2, 5))

        for n in nums:
            with self.subTest(n=n):

                start = time.time()
                (runtime, total) = timed_sum(n)
                end = time.time()

                self.assertGreater(runtime, 0)
                self.assertAlmostEqual(end-start, runtime, places=5)
                self.assertEqual(total, math_sum(n))

    def test_number(self):
        '''Test the number parameter to the timeit decorator'''
        
        max_exp = 10
        numbers = (2**i for i in range(max_exp+1))

        n = 25

        for number in numbers:
            with self.subTest(number=number):
                
                counter = [0]

                @timeit(number=number)
                def count_calls(cc):
                    cc[0] = cc[0] + 1

                (runtime, _) = count_calls(counter)
                self.assertEqual(counter[0], number)

    def test_timer(self):
        '''Test the timer parameter to the timeit decorator'''
        
        def counting_timer(cc):
            def timer():
                cc[0] = cc[0] + 1
                return time.time()
            return timer

        nums = (10**i for i in range(2, 5))

        for n in nums:

            counter = [0]

            with self.subTest(n=n):
                
                @timeit(timer=counting_timer(counter))
                def timed_sum(n):
                    return sum_function(n)

                timed_sum(n)
                self.assertEqual(counter[0], 2)

if __name__ == '__main__':
    
    unittest.main()
