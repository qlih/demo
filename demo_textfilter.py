#!/usr/bin/env python3
   # encoding: UTF-8
# 文本行格式化 处理器
# demo_remove_ad_in_firstline，删除章节头部广告

import re
import json

class TextFilter():
	data=[]		#行处理模式
	cstr=''	#串模式

	def remove_lines_at_head(self):
		f = open('demo_remove_ad_at_firstline.txt', 'r') # 读文件错，就报错，因为默认要有这个空文件。
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
				else:
					pass


	def remove_words(self):
		f = open('demo_remove_words.txt', 'r')
		rules=f.readlines()
		f.close()

		for j in range(len(rules)):
			rule = rules[j].strip()	#去掉换行符和空格
			if rule=="":	#遇到空行就结束处理，这是一个调试技巧。
				break
			for i in range(len(self.data)) :
				self.data[i] = self.data[i].replace(rule,'')	#没测试换行符。这里需要记录日志吧？


	def remove_lines_in_file(self):
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
				else:
					pass


	def parse_regx(self):
		f=open('demo_regx.txt','r')
		rules=f.readlines()
		f.close()

		for rule in rules:
			regx=rule.strip()
			if regx =="" :
				break
			self.cstr=re.sub(regx,'',self.cstr)
		self.cstr=re.sub('\n\n*','\n',self.cstr)
		print(self.cstr)
		self.data=self.cstr.split('\n\n')


	def load_regx(self,_regx_file='demo_regx.json'):
		with open('d_regx_file', 'r') as f:
			rules = json.load(f)
		f.close()
		return rules


	def json_regx(self, _cstr=''):
		self.cstr=_cstr
		rules = load_regx()

		cn=''
		for rule in rules:
			search_regx=rule['search']
			replace_regx=rule['replace']
			if(replace_regx!="" and replace_regx!=None):
				regx_count=rule['count']
				regx_flag=rule['flag']
				cn,number=re.subn(search_regx,replace_regx,self.cstr,regx_count,regx_flag)
			else:
				cn,number=re.subn(search_regx,'',self.cstr)
			self.cstr=cn
			print(number,rule)
		#self.data=self.cstr.split('\n\n')


	def __init__ (self, _cstr=''):

		#self.data = _data
		#self.cstr=''.join(self.data)
		self.cstr=_cstr
		#self.remove_lines_at_head()
		#self.remove_lines_in_file()
		#self.remove_words()
#
		self.json_regx()


if __name__ == '__main__':

	import os
	from demo_lib import GetFileNameAndExt

	fullname='demo_charpter.txt'
	f = open(fullname, 'r')
	tf=TextFilter()
	tf.load_regx()
	tf.json_regx(f.read())
	#lines=f.readlines()
	f.close()

	(shotname,extension) = GetFileNameAndExt(fullname)	#应该处理工作目录

	f=open(shotname+'$'+extension, 'w')  #默认存盘的字符编码是utf8，mac下测试。
	f.write(tf.cstr)
#	f.writelines(tf.data)
	f.close()


