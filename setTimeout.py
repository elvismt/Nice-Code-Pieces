# utils.py

import threading
from functools import wraps

def delay(delay=0.):
    """
    Decorator delaying the execution of a function for a while.
    """
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap


#main.py

from utils import delay

@delay(3.0)
def my_func(arg1, arg2):
    print arg1, arg2

if __name__ == '__main__':
    my_func('Hello', 'world')
