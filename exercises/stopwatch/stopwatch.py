import time
from time import sleep

def stopwatch():
    now = time.time()
    now_readable = time.ctime()
    print('This is the unix time: ', now)
    print('In another word:', now_readable)
    sleep(5)
    later =time.time()
    later_readable = time.ctime()
    time_lapse = later - now
    print('This is another unix time:', later)
    print('In another word for second unix time:', later_readable)
    print('This is the difference between two times:',round(time_lapse))
stopwatch()