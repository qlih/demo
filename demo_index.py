#!/usr/bin/env python3
   # -*- coding:utf-8 -*-
# biquge.tw 处理器
#
# 目录页读取测试，没完成。
import requests

from html.parser import HTMLParser
from demo_lib import CharpterTitleFilter
from demo_charpter import CharpterContentParser
from demo_textfilter import TextFilter

class IndexParser(HTMLParser):
	re={}#放置结果
	properties={}
	ch_url=''
	meta_flag=''#标志，<meta/>
	a_flag=0 #标志，<a>...</a>

	website = 'http://www.biquge.tw'

	def handle_starttag(self, tag, attrs):
		if tag=='a':#目标标签
			for attr in attrs:
				if attr[0]=='style':#目标标签具有的属性
					self.a_flag=1 # 找到 <a style=""
					continue
				if attr[0]=='href' and self.a_flag==1:
					self.ch_url=self.website + attr[1] # 记录 href 的值
					self.a_flag=2 # 找到第二个参数了 href
					break
		#elif tag=='dt':
		#	column_flg = 1
		else:
			pass

	def handle_data(self, data):
		if self.a_flag==2:
			cn = CharpterTitleFilter(data.strip())	#格式化章节号
			if cn == None : # 没有格式化
				self.re[self.ch_url] = data.strip()
			else:
				self.re[self.ch_url] = cn
			self.a_flag=0#重置标志，进行下次迭代
		#elif self.dt_flag==1:
		#	str_colum=data.strip()	#卷的名字都不正规，不再自动处理了。
		#	修订 re 目录树
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


if __name__ == '__main__':
	my=IndexParser()

	index_url = ''
	ch_from = ch_to = 0
	#命令行不用完整的web地址，因为爬虫只识别当前的网址。
	#	usage： 书目网址 起始章节号 最终章节号
	# if len(sys.argv) > 1:
	#	index_url = sys.argv[1]
	#	r=requests.get(url=index_url)
	#	my.feed(r.text)
	#	if len(sys.argv) >3:
	#		ch_from = sys.argv[2]
	#	elif len(sys.argv) >2:
	#		ch_to = sys.argv[3]
	# else:
	# try
	my.feed(open('demo_index.html').read())
	# sys.exit()

	workdir = 'documents/'+'proj_name'	#documents 来自 配置？
	# clean()	# 清除所有自身产生的临时文件

#	print(my.re)
	charpter = CharpterContentParser()
	for ch_url in my.re: #这里要用多线程2-5个。
		r = requests.get(url=ch_url)
		charpter.re=[]
		charpter.feed(r.text)
		tmpfile = '.'+os.sep+'$'+os.sep+my.re[ch_url]+'$.txt'
		f=open(tmpfile,'w')
		f.writelines(charpter.re)
		f.close()

		tf=TextFilter(''.join(charpter.re)) #还没处理卷号，卷是目录名，也放在数组里
		#如果文件存在就不要覆盖了！因为很多已经被重复编辑过的。
		f = open('./1/'+my.re[ch_url]+'.txt','w')  #默认存盘的字符编码是utf8，mac下测试。
		f.write(tf.cstr)
		f.close()
		print (ch_url)#url for text
		print (my.re[ch_url])#filename
#	print(len(my.re))
	charpter.close()
#
	print(my.properties)
	print(len(my.properties))
