# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-17 22:34:04


import threading


class MyChannel(object):

    def __init__(self, callback=None):
        self._channel = []
        self._lock = threading.Lock()
        self.callback = callback

    @property
    def callback(self):
        print ('trigger')
        return self._callback

    @callback.setter
    def callback(self, cb):
        if hasattr(cb, '__call__'):
            self._callback = cb
            if len(self._channel):
                cb(self)
        else:
            self._callback = None

    @property
    def ch(self):
        if len(self._channel):
            with self._lock:
                return self._channel.pop(0)
        else:
            return None

    @ch.setter
    def ch(self, item):
        with self._lock:
            self._channel.append(item)
        self.callback and self.callback(self)

if __name__ == '__main__':
    ch = MyChannel()
    ch.ch = 1
    print(ch._channel) 
    # [1]
    s = ch.ch
    print(s)
    # 1
    ch.ch = 2
    print(s)
    # 1
    print(ch.ch)
    # 2
    print(ch._channel)
    # []
    print(ch.ch)
    # None
