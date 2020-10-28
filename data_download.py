#In[]:
# coding=utf-8
import collections
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
leibies = zong_session.html.find(sel)[1].find("a")

leibie_dfs = collections.OrderedDict() 

print([leibie_temp.text for leibie_temp in leibies])

writer = pd.ExcelWriter('./yingyangchengfen.xlsx')

for leibie in leibies:
    #leibie = leibies[0]
    leibie_name, leibie_sub_url = (leibie.text, list(leibie.links)[0])
    if leibie_name == '药食及其它':
        continue
    leibie_url = '{}{}'.format(url, leibie_sub_url)
    leibie_session = session.get(leibie_url)
    shiwu_sel = "body > div#main > div#main_left > div.kuang > div#main_content > ul.list > li"
    shiwues = leibie_session.html.find(shiwu_sel)
    shiwu_df = pd.DataFrame()
    for shiwu in shiwues:
        #shiwu = shiwues[0]
        shiwu_dict = dict()
        shiwu_name = shiwu.text
        #import pdb;pdb.set_trace()
        shiwu_dict['名称'] = shiwu_name
        shiwu_sub_url = list(shiwu.links)[0]
        shiwu_yinyangchengfen_url = '{}{}'.format(url, shiwu_sub_url)
        shiwu_dict['url'] = shiwu_yinyangchengfen_url
        shiwu_yinyangchengfen_session = session.get(shiwu_yinyangchengfen_url)
        shiwu_yinyang_sel = "body > div#main > div#main_left > div.kuang > div#main_content > table > tr"
        yinyangchengfens = shiwu_yinyangchengfen_session.html.find(shiwu_yinyang_sel)
        for yinyangchengfen in yinyangchengfens:
            #yinyangchengfen = yinyangchengfens[0]
            yinyangchengfen = yinyangchengfen.text.split('\n')
            shiwu_dict[yinyangchengfen[0]] = yinyangchengfen[1]
            shiwu_dict[yinyangchengfen[2]] = yinyangchengfen[3]
        shiwu_df = shiwu_df.append(shiwu_dict, ignore_index=True)
    shiwu_df.set_index(['名称'], inplace=True)
    leibie_dfs[leibie_name] = shiwu_df
    shiwu_df.to_excel(writer, sheet_name=leibie_name)
    #print(shiwu_df)
    writer.save()
    print(leibie_name)
    #break
#In[]
temp = shiwu_df.append(shiwu_dict, ignore_index=True)
temp.set_index(['名称'], inplace=True)
temp