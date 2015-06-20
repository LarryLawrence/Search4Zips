#reg = r'href="(.\.zip)"'
import re
import urllib
import time
import urllib2


def getHtml(url,headers):
    r = urllib2.Request(url,headers)
    page = urllib.urlopen(url)
    html = page.read()
    return html
	

def getZip(html):
    reg = r'href="(.+?\.zip)"'
    Zipre = re.compile(reg)
    ziplist = re.findall(Zipre,html)
    return ziplist        

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }	
qianyao = 'http://www.xxxzj.com/rom/'
f=open('out.txt','w')
for number in range(3201, 4499+1):
	theExactUrl = qianyao + str(number) + '.htm'
	html = getHtml(theExactUrl,headers)
	print getZip(html)
	print>>f,getZip(html)
	time.sleep(1)
	


