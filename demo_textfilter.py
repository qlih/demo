#!/usr/bin/env python3
   # encoding: UTF-8
# 文本行格式化 处理器
# demo_remove_ad_in_firstline，删除章节头部广告

class TextFilter():
	data=[]

	def demo_remove_lines_at_head(self):
		f = open('demo_remove_ad_at_firstline.txt', 'r')
		rules=f.readlines()
		f.close()
		for j in range(len(rules)):
			rule = rules[j].strip()
			if rule=="":
				break
			for i in range(len(self.data)) :
				if self.data[i].strip().find(rule)==0 : #str.find("")永远返回true
					del(self.data[i]) # 删了一个，列表短了。
					#删除随后的空行
					while i<len(self.data) and self.data[i].strip()=="": # i<len(data)防止下标越界
						del(self.data[i])
					break	


	def demo_remove_words(self):
		f = open('demo_remove_words.txt', 'r')
		rules=f.readlines()
		f.close()

		for j in range(len(rules)):
			rule = rules[j].strip()	#去掉换行符和空格
			if rule=="":	#遇到空行就结束处理，这是一个调试技巧。
				break
			for i in range(len(self.data)) :
				self.data[i] = self.data[i].replace(rule,'')	#没测试换行符。这里需要记录日志吧？


	def demo_remove_lines_in_file(self):
		f = open('demo_remove_ad_at_tail.txt','r')
		rules=f.readlines()
		f.close()

		for j in range(len(rules)):
			rule = rules[j].strip()	#去掉换行符和空格
			if rule=="":	#遇到空行就结束处理，这是一个调试技巧。
				break
			for i in range(len(self.data)) :
				if self.data[i].strip().find(rule)==0 : #str.find("")永远返回true
					del(self.data[i]) # 删了一个，列表短了。
					#删除随后的空行
					while i<len(self.data) and self.data[i].strip()=="": # i<len(data)防止下标越界
						del(self.data[i])
					break	


	def __init__ (self, fullname='demo_charpter.txt'):
		import os

		f = open(fullname, 'r')
		self.data = f.readlines()
		f.close()

		self.demo_remove_lines_at_head()
		self.demo_remove_words()
		self.demo_remove_lines_in_file()

		(filepath,tempfilename) = os.path.split(fullname);
		(shotname,extension) = os.path.splitext(tempfilename);

		f = open(shotname+'$'+extension, 'w')  #默认存盘的字符编码是utf8，mac下测试。
		f.writelines(self.data)
		f.close()


if __name__ == '__main__':
#	tf=TextFilter('demo.txt')
	tf=TextFilter()
	

