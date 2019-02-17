# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-17 22:49:34


import time
import threading
from datetime import datetime
from main import MyChannel


class BaseModel(object):
    def __init__(self, ch):
        self.ch = ch

class Producer(BaseModel):
    def __init__(self, ch):
        super(Producer, self).__init__(ch)
        self._sleep = 1

    def run(self):
        self.ch.ch = datetime.now()

    def keep(self):
        start = time.time()
        while True:
            time.sleep(self._sleep)
            if time.time() > start + 6:
                return
            self.run()


class Customer(BaseModel):
    def __init__(self, ch):
        super(Customer, self).__init__(ch)
        self._sleep = 1

        
    def run(self, ch=None):
        ch = ch or self.ch
        s = ch.ch
        while s:
            print (s)
            s = ch.ch

    def keep(self):
        start = time.time()
        while True:
            if time.time() > start + 10:
                return
            self.run()

class ChannelTest(object):
        
    def delay(self):
        ch = MyChannel()
        c, p = Customer(ch), Producer(ch)
        p = threading.Thread(name='pro', target=p.keep)
        p.start()
        time.sleep(7)
        ch.callback = c.run

    def trigger(self):
        ch = MyChannel()
        c, p = Customer(ch), Producer(ch)
        ch.callback = c.run
        p = threading.Thread(name='pro', target=p.keep)
        p.start()

    def watching(self):
        ch = MyChannel()
        c, p = Customer(ch), Producer(ch)
        p = threading.Thread(name='pro', target=p.keep)
        c = threading.Thread(name='pro', target=c.keep)
        p.start()
        c.start()

if __name__ == '__main__':
    ct = ChannelTest()
    # ct.delay()
    # ct.trigger()
    ct.watching()
