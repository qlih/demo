#!/usr/local/bin/python3
   # -*- coding:utf-8 -*-  
# biquge.tw 处理器
# website = 'http://www.biquge.tw'
# 目录页读取测试，没完成。

from html.parser import HTMLParser

class MyParser(HTMLParser):
    re={}#放置结果
    properties={}
    ch_url=''
    meta_flag=''#标志，<meta/>
    a_flag=0 #标志，<a>...</a>

    def handle_starttag(self, tag, attrs):
        if tag=='a':#目标标签
            for attr in attrs:
                if attr[0]=='style':#目标标签具有的属性
                    self.a_flag=1 # 找到 <a style=""
                    continue
                if attr[0]=='href' and self.a_flag==1:
                    self.ch_url=attr[1] # 记录 href 的值
                    self.a_flag=2 # 找到第二个参数了 href
                    break
        else:
            pass
  
    def handle_data(self, data):
        if self.a_flag==2:
            self.re[self.ch_url] = data.strip()
            self.a_flag=0#重置标志，进行下次迭代
        else:
            pass

    def handle_startendtag(self, tag, attrs):
        self.meta_flag=''
        if tag=='meta':
            for attr in attrs:
                if attr[0]=='property' and attr[1] in ['og:novel:author','og:novel:book_name','og:novel:update_time','og:description','og:novel:status']:
                    self.meta_flag=attr[1]
                    continue
                if attr[0]=='content' and self.meta_flag!='':
                    self.properties[self.meta_flag] = attr[1]
                    self.meta_flag = ''
                    break
        else:
            pass


my=MyParser()
my.feed(open('demo_index.html').read())
print(my.re)
print(len(my.re))
print(my.properties)
print(len(my.properties))
