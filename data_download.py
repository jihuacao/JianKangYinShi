# coding=utf-8
#In[]:
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://yingyang.51240.com/'

zong_session = session.get(url)

##In[]:
#import urllib
#import lxml.html
#
#soup = BeautifulSoup(url, 'html.parser')
#html = urllib.request.urlopen(url).read()
#
#tree = lxml.html.fromstring(html)
#
#tree.cssselect('body > div#main')
#
#In[]:
sel = 'body > div#main > div#main_left > div.kuang > div#main_content > div.xiaoshuomingkuang_neirong > p'
#r.html.find('body')[0].find('div')
c = zong_session.html.find(sel)[1]

leibies = c.find('a')
leibie_urls = dict()

for leibie in leibies:
    leibie_urls[leibie.text] = leibie.url
    pass

for k, v in leibie_urls:
    leibie_url = '{}{}'.format(url, v)
    leibie_session = session.get(leibie_url)
    leibie_session