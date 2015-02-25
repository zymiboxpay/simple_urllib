#  -*- coding: utf-8 -*-
# !/usr/bin/python

import urllib2
import urllib
import chardet
import sys
import cookielib
import re

auth_url = 'http://172.30.0.161/zentao/user-login.html'
home_url = 'http://172.30.0.161/zentao/my'

#保存cookie的文件
cookieFileName = "fileCookieJar.txt"

# 登陆用户名和密码
data={
    "account":"",
    "password":"",
    "keepLogin[]": "on",
    "referer":""
}
# urllib进行编码
post_data=urllib.urlencode(data)
# 发送头信息
headers ={
    "Host":"172.30.0.161", 
    "Referer": "http://172.30.0.161/zentao/user-login.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"
}
# 初始化一个CookieJar来处理Cookie
cookie=cookielib.MozillaCookieJar()

# 读取文件中的cookie
cookie.load(cookieFileName)

# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 获取cookie
# req=urllib2.Request(auth_url,post_data,headers)
# result = opener.open(req)

#保存cookie
# cookie.save()



# 访问主页 自动带着cookie信息
content = opener.open(home_url).read()

#获取系统编码
typeEncode = sys.getfilesystemencoding()
#获取网页编码
infoencode = chardet.detect(content).get('encoding','utf-8')

#先将网页编码转换为unicode再转为系统编码
html = content.decode(infoencode,'ignore').encode(typeEncode)

# 显示结果
print html
