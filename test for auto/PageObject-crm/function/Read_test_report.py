#coding:utf-8
import os
def read_test_report(report_path):
    #当前文件的父级目录
    #filedir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    #存储报告的路径
    #filepath = filedir + "\\report"

    os.chdir(report_path)
    #选出最新的测试报告
    reports = os.listdir(os.getcwd())
    reports.sort(key=lambda fn:os.path.getatime(os.getcwd() + "\\" + fn))
    last_report = reports[-1]
    print last_report
    try:
        fp = open(last_report,'r')
        content = fp.read()
        print u"读取报告成功"
        return content
    except Exception as msg:
        print "error:%s"%msg


if __name__ == '__main__':
    # 当前文件的父级目录
    filedir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    # 存储报告的路径
    filepath = filedir + "\\report"
    read_test_report(filepath)