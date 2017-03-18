#encoding:utf-8
import os
from urllib2 import *
import json
import re
import sys

link1="http://zidian.51240.com/pinyinl/"
tag1="""<div id="main_content">.+?</table></div>
</div>"""
tag2="""<li><a href=.+?</a></li>"""
tag3="""<div class="list_zidian_zi">.+?组词</a></div></div>"""
tag4="""<div class="list_zidian_zi_zi">.+?</div>"""
tag5='href="http://bihua.51240.com'+"""/.+?笔画</a></div>"""
tag6="""<td bgcolor="#F5F5F5" align="center">笔画</td>
<td bgcolor="#FFFFFF" colspan="2">.+?</td>
</tr>"""
tag7="""<img src=.+?/>"""

o=open("bihua.txt",'w')

content1=urlopen(link1).read()
content2=re.findall(tag1,content1)[0]
content3=re.findall(tag2,content2)
#print(content3)
#print(len(content3))
for i in range(0,len(content3)):
    content3[i]="http://zidian.51240.com"+content3[i].split('"')[1]

#print(content3)
########just a test
for target1 in content3:
    content4=urlopen(target1).read()
    content5=re.findall(tag1,content4)[0]
    #print(content5)
    content6=re.findall(tag3,content5)

    content7=[]

    for i in range(0,len(content6)):
        p=re.findall(tag4,content6[i])[0].split('</div>')[0].split('<div class="list_zidian_zi_zi">')[1]
        content7.append(p)
    #print(content7)
    #print(len(content7))
    content8=[]
    for i in range(0,len(content6)):
        p=re.findall(tag5,content6[i])[0].split('href')[1].split('"')[1]
        content8.append(p)

    for i in range(0,len(content7)):
        target2=content8[i]
        try:
            content9=urlopen(target2).read()
        except:
            print(content7[i]+"failed,might be not found")
            continue
        try:
            content10=re.findall(tag6,content9)[0]
            content11=re.findall(tag7,content10)
            for j in range(0,len(content11)):
                content11[j]=content11[j].split('alt="')[1].split('"')[0]
            bihua=str(','.join(content11))
            o.write(content7[i]+':'+bihua+"\n")
        except:
            print(content7[i]+"failed,might be index error")
            pass
#print(content6)
#print(len(content6))

#print(content8)
#print(len(content8))

"""
for i in range(0,len(content3)):
    content6[i]="http://zidian.51240.com"+content6[i].split('"')[1]
print(content6)
print(len(content6))
print(content7)
print(len(content7))
"""

#<div class="list_zidian_zi"><div class="list_zidian_zi_pinyin">ā</div><div class="list_zidian_zi_zi">啊</div><div class="list_zidian_zi_you"><a target="_blank" href="/e5958a__zidianchaxun/">字典</a></div><div class="list_zidian_zi_you"><a target="_blank" href="http://bihua.51240.com/e5958a__bihuachaxun/">笔画</a></div><div class="list_zidian_zi_you"><a target="_blank" href="http://zuci.51240.com/%E5%95%8A__zuci/">组词</a></div></div>
#<div class="list_zidian_zi_you"><a target="_blank" href="http://bihua.51240.com/e59096__bihuachaxun/">笔画</a></div>
