# -*-coding: "utf-8"-*-

"""
# File:        threadtest.py
# Author:      "liyi"
# CreateTime:  2022/7/15 16:03
# Version:     python 3.6
# Description:   
"""
import threading
import datetime
import time
from util.kill_thread import stop_thread

def test(i, t):
    print([i, t])
    t0 = threading.Timer(t, test, (i,t, ))
    t0.start()


if __name__ == '__main__':
    # for i in range(3):
    #     p0 = threading.Thread(target=test, args=(i,3, ))
    #     p0.start()
    #
    # for i in range(3,5):
    #     if i==4:
    #         time.sleep(6)
    #     p0 = threading.Thread(target=test, args=(i, 6, ))
    #     p0.start()
    # p0 = threading.Thread(target=test, args=(1,))
    # p0 = threading.Timer(5, function=test, args=(1, ))
    # p0.start()
    out_dict = {}
    for i in range(3):
        out_dict.update({str(i):[i]})
    print(out_dict)


# def run():
#     print(datetime.datetime.now())
#     r_t01 = threading.Timer(1, run)
#     r_t01.start()
#
#
# if __name__ == '__main__':
#     t01 = threading.Thread(target=run)
#     t01.start()