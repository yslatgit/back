#coding=utf-8
import yaml
import os

#获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
#获取yaml文件路径
yamlPath = os.path.join(curPath,"cfg.yaml")

f = open(yamlPath,'r')
cfg = f.read()
print (type(cfg))
print cfg

d1 = yaml.load(cfg)
print d1