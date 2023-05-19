import time

def timeit(timer=time.time, number=1):
    '''
    Higher order decorator to time a given function
    :param timer: Callable type whose __call__ function takes no arguments.
        Returns a positive, monotonically increasing number indicating the time
    :param number: number of times to run the decorated function
    '''
    def inner_wrapper(f):
        def timeit_wrapper(*args, **kwargs):
            
            start = timer()
            for _ in range(number):
                rv = f(*args, **kwargs)
            stop = timer()

            return (stop - start, rv)
        return timeit_wrapper
    return inner_wrapper
