import requests
import urllib
import re

class aoxiang:
	def __init__(self, name, passwd):
		self.loginurl = 'http://us.nwpu.edu.cn/eams/login.action'
		self.examurl = 'http://us.nwpu.edu.cn/eams/stdExamTable.action'
		self.param = {
			'username': name,
			'password': passwd,
		}

	def get(self):
		r = requests.Session()
		s = r.post(url=self.loginurl, data=self.param)
		# print(s.text)
		pattern = re.compile('我的账户*')
		a = pattern.findall(s.text)
		# print (a)
		return a
