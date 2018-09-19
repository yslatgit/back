#encoding:utf-8
import sys
import os

def screen_android_to_windows():
    name = sys.argv[1]
    #print name
    os.popen("adb shell /system/bin/screencap -p /sdcard/%s.png"%name)
    os.popen("adb pull /sdcard/%s.png D:\screen\%s.png"%(name,name))
if __name__ == '__main__':
    screen_android_to_windows()