#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自紫星的测试邮件', '564480667@qq.com', '2963007588@qq.com'
    text_content = '欢迎访问百度'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.baidu.com</a>,这里是百度</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

