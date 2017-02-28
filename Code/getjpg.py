#coding=utf-8
import urllib   #Urllib 模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据
import re   #re模块主要包含了正则表达式

#urlretrieve用法
# urllib.urlretrieve(url[, filename[, reporthook[, data]]])
# 参数说明：
# url：外部或者本地url
# filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
# reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
# data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()  #read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。执行程序就会把整个网页打印输出
    return html

# 用于在获取的整个页面中筛选需要的图片连接
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre,html)       #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        # 这里的核心是用到了urllib.urlretrieve()方法，直接将远程数据下载到本地
        urllib.urlretrieve(imgurl,'C:\Users\htc\Desktop\png\\' '%s.jpg' % x)
        x+=1
urls=raw_input("please enter the URL:")
html = getHtml(urls)
# html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)