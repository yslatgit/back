#coding:utf-8

f = open('mobile.txt','w+')
b = 15100000000
for i in range(2000):
    msg = int(i)+int(b)
    print msg
    f.write('%s\n'%msg)
