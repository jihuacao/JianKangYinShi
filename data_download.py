# coding=utf-8
#In[]:
import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://yingyang.51240.com'

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
leibies = zong_session.html.find(sel)[1]

leibie_dfs = dict()

#for leibie in leibies:
leibie_name, leibie_sub_url = leibie.text, list(leibie.links)[0]
leibie_url = '{}{}'.format(url, v)
leibie_session = session.get(leibie_url)
shiwu_sel = "body > div#main > div#main_left > div.kuang > div#main_content > ul.list > li"
shiwues = leibie_session.html.find(shiwu_sel)
shiwu_df = pd.DataFrame()
#for shiwu in shiwues:
shiwu = shiwues[0]
shiwu_dict = dict()
shiwu_name = shiwu.text
shiwu_dict['名称'] = shiwu_name
shiwu_sub_url = list(shiwu.links)[0]
shiwu_yinyangchengfen_url = '{}{}'.format(url, shiwu_sub_url)
shiwu_dict['url'] = shiwu_yinyangchengfen_url
print(shiwu_yinyangchengfen_url)
shiwu_yinyangchengfen_session = session.get(shiwu_yinyangchengfen_url)
shiwu_yinyang_sel = "body > div#main > div#main_left > div.kuang > div#main_content > table > tr"
yinyangchengfens = shiwu_yinyangchengfen_session.html.find(shiwu_yinyang_sel)
#for yinyangchenfen in yinyangchengfens:
yinyangchengfen = yinyangchengfens[0]
yinyangchengfen = yinyangchengfen.text.split('\n')
shiwu_dict[yinyangchengfen[0]] = yinyangchengfen[1]
shiwu_dict[yinyangchengfen[2]] = yinyangchengfen[3]
shiwu_df = shiwu_df.append(shiwu_dict)
shiwu_df.set_index(['名称']， inplace)
#In[]
temp = shiwu_df.append(shiwu_dict, ignore_index=True)
temp.set_index(['名称'], inplace=True)
temp