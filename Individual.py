# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:22:05 2022

@author: Brandon
"""

class Individual(object):
    def __init__(self, stats, start, target):
        self.stats = stats
        self.index = start
        self.counter = 0
        self.target = target
        
    def getStats(self):
        return self.stats
    
    def increment(self):
        self.counter = self.counter + 1