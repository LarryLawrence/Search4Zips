#reg = r'href="(.\.zip)"'
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
	

def getZip(html):
    reg = r'href="(.+?\.zip)"'
    Zipre = re.compile(reg)
    ziplist = re.findall(Zipre,html)
    return ziplist        

qianyao = 'http://www.xxxzj.com/rom/'
f=open('out.txt','w')
for number in range(500, 999+1):
	theExactUrl = qianyao + str(number) + '.htm'
	html = getHtml(theExactUrl)
	print getZip(html)
	print>>f,getZip(html)
	


