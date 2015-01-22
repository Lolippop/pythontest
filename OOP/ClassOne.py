#coding:utf-8
__author__ = 'oliver'
class Calculator(object):
    def __init__(self):
        self.current = 0
        self.result = 0
    def add(self,amount):
        self.current += amount
    def getCurrent(self):
        return self.current
    def getResult(self):
        return self.result + self.current

