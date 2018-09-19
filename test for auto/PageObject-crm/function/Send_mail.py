#coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import Read_test_report
def send_mail(report_path):
    """mdnzwyosfphsbaif"""
    my_sender = '986725816@qq.com'
    my_pass = 'mdnzwyosfphsbaif'
    receivers = ['yangsonglin@mofanghr.com']
    html = Read_test_report.read_test_report(report_path)
    try:
        #msg = MIMEText(u'自动化','plain','utf-8') 文本邮件正文
        msg = MIMEText(html,'html','utf-8') #发送html正文的邮件
        msg['From'] = formataddr(["林",my_sender])
        msg['To'] = formataddr(["杨松林",receivers])
        msg['Subject'] = u"自动化测试报告"
        print "1"
        server = smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(my_sender,my_pass)
        server.sendmail(my_sender,[receivers,],msg.as_string())
        print "2"
        print u"发送邮件成功"
        server.quit()
    except Exception as ms:
        print "error:%s"%ms


if __name__ == '__main__':
    # 当前文件的父级目录
    filedir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    # 存储报告的路径
    filepath = filedir + "\\report"
    send_mail(filepath)