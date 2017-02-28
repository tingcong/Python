#coding=utf-8
import urllib2

print urllib2.urlopen('http://www.baidu.com').read()

print '######################################1.URLError##################################################'
req = urllib2.Request('http://www.baibai.com')

try:
    urllib2.urlopen(req)

except urllib2.URLError, e:
    print e.reason
print '######################################2.HTTPError#################################################'

req = urllib2.Request('http://bbs.csdn.net/callmewhy')

try:
    urllib2.urlopen(req)
except urllib2.URLError, e:

    print e.code

print '######################################3.Wrapping#################################################'
from urllib2 import Request, urlopen, URLError, HTTPError

req = Request('http://bbs.csdn.net/callmewhy')

try:

    response = urlopen(req)
except HTTPError, e:

    print 'The server couldn\'t fulfill the request.'

    print 'Error code: ', e.code
except URLError, e:

    print 'We failed to reach a server.'

    print 'Reason: ', e.reason
else:
    print 'No exception was raised.'
    # everything is fine

print '######################################.info()：###################################################'

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()


print '######################################.geturl()：###################################################'
# 这个返回获取的真实的URL，这个很有用，因为urlopen(或者opener对象使用的)或许会有重定向。获取的URL或许跟请求URL不同
old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)
print 'Old url :' + old_url
print 'Real url :' + response.geturl()



