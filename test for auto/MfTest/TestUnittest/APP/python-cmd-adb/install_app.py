#coding:utf-8
import sys
import os
def installapp():
    name = sys.argv[1]
    print name
    os.popen(r"adb install -r %s"%name)

if __name__ == '__main__':
    try:
        installapp()
        print "Sucess"
    except Exception as msg:
        print u"有异常%s"%msg