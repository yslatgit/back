#coding:utf-8
import math
"""一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？"""
def xyz(x):
    return x * x

def test():
    for i in range(1,100):
        x = math.sqrt(i+100)
        y = math.sqrt(i+268)
        if xyz(x) == (i+100) and xyz(y) == (i+268):
            print i

if __name__ == '__main__':
    print test()