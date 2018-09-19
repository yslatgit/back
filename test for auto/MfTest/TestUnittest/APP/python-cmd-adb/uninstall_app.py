#coding:utf-8
import sys
import os
import re
def uninstallapp():
    name = sys.argv[1]
    print name
    #result接收cmd命令的返回值--一片内存地址
    result = os.popen("aapt dump badging %s"%name)
    #fp从内存地址中读取一行
    fp = result.readline()
    #通过正则表达式提取相应的包名
    activity_name = re.search("\'(.*?)\'",fp,re.M|re.I)
    f_name = activity_name.group(1)
    print f_name

    os.popen(r"adb uninstall %s"%f_name)

if __name__ == '__main__':
    try:
        uninstallapp()
        print "Sucess"
    except Exception as msg:
        print u"有异常%s"%msg