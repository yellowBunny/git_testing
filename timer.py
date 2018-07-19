import time
import seba

def stoper(func, *args):
    start = time.time()
    func()
    stop = time.time()
    return stop - start








