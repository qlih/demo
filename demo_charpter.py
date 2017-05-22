#!/usr/local/bin/python3
   # -*- coding:utf-8 -*-  
# www.biquge.tw 处理器
# 章节读取测试

from html.parser import HTMLParser

class CharpterContentParser(HTMLParser):
    re=[] #放置结果
    flg=0 #标志，用以标记是否找到 <div id="content"> 标签。0：在<div>以外，1:在<div>以内，2:在<div>以内，并且找到了内嵌的<br/>
    def handle_starttag(self, tag, attrs):
        if tag=='div':#目标标签
            for attr in attrs:
                if attr[0]=='id' and attr[1]=='content' :#目标标签具有的属性
                    self.flg=1 # 找到 <div id="content">
                    break
        else:
            pass
  
    def handle_data(self, data):
        if self.flg>0:  #self.flg = 1 时，是<div>之后的第一行，例子中的第一行和最后一行通常是广告，但也有极少数是正文。因此也收下。
            data = data.strip()
            if data != "" : #非空行
               self.re.append("　　"+data) #行头增加了2个全角空格。
            self.re.append("\n") #用unix换行替换了<br/>
        else:
            pass

    def handle_endtag(self, tag):
        if self.flg==2 and tag=='div':  # 处理了<br/>以后，遇到了</div>
            self.flg=0  # 本div tag 处理结束
        else:
            pass

    def handle_startendtag(self, tag, attrs):
        if self.flg==2: # 表示还在 <div> 标签中，但是正在处理 <br/>
            pass
        elif tag=='br' and self.flg==1:
            self.flg=2 # 在<div>...</div>之间找到了<br/>，div的状态转换到‘2’。
        else:
            pass


if __name__ == '__main__':

    my=CharpterContentParser()
    my.feed(open('demo_charpter.html').read())

    f = open('demo_charpter.txt', 'w')  #默认存盘的字符编码是utf8，mac下测试。
    f.writelines(my.re)
    f.close()

    my.close()

