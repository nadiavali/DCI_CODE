import time
from time import sleep

def stopwatch():
    n = time.time()
    m = time.ctime()
    print('This is unix time: ', n)
    print('In another word:', m)
    sleep(3)
    u =time.time()
    t = time.ctime()
    z = u - n
    print('This is another unix time:', u)
    print('In another word for second unix time:', t)
    print('This is the difference between two times:',z)
stopwatch()