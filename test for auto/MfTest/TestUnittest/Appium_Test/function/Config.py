#coding:utf-8
import os
import time
from threading import Thread


def get_app_name():
    app_path = os.getcwd() + "\\appfortest"
    apps = os.listdir(app_path)
    for i in apps:
        if 'apk' in i:
            return app_path + "\\" + i
        else:
            return "can't find app"

#安装APP·1
def _install_app():
    appName = get_app_name()
    os.system('adb install -r %s'%appName)

#安装APP·2
def _inputEvent():
    i = 1
    while i<10:
        os.popen("adb shell input tap 1000 1500")
        i = i + 1
        time.sleep(10)
#安装app
def install():
    t1 = Thread(target=_install_app)
    t2 = Thread(target=_inputEvent)
    t1.start()
    t2.start()

if __name__ == '__main__':
    install()

