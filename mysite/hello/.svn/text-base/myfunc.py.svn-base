
import urllib
import sae.storage
# def cbk(a, b, c):
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print '%.2f%%' % per
# url = 'http://www.sina.com.cn'
# local = 'z:\sina.html'
# urllib.urlretrieve(url, local, cbk)


def curl():
    fd = urllib.urlopen('http://www.baidu.com')
    return fd.info()


def store():
    s=sae.storage.Client()
    #d=s.list_domain()
    n=s.list("code")
    fileno=[]
    for i in n:
        filename=i['name']
        url=s.url("code",filename.encode('utf-8'))
        #url=url.decode('utf-8')
        fileno.append((filename,url))
        #fileno.append(s.get(d,filename))
    return fileno