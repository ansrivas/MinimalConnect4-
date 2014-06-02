# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:39:00 2014

@author: ankur
"""
#A sample profiler for our code, usage give below

'''
Sample Usage
def printing():
    print "hello"
timer = timewith('')
printing()
t = timer.checkpoint('')
print "timetaken" , t
'''


import time

class timewith():
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print '{timer} {checkpoint} took {elapsed} seconds'.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip()
        return self.elapsed

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
        pass


