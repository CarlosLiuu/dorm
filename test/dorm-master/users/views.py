# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms  
from users.models import User
from users.form import LoginForm
from users.form import sub
import re
# Create your views here.

def login(req):
	if req.method == 'POST':
		username=req.POST['username']
		password=req.POST['password']
		if not (password and username):
			return render(req,'error.html',{'error':'学号、密码均不能为空','url':'/denglu/'})
		user=User.objects.filter(username=username,password=password)
		if user:
			sub1=sub(username)
			return sub1.index(req)
		else:
			return render(req, 'error.html', {'error': '该用户不存在', 'url': '/denglu/'})
		return render(req,'login.html')
	
def register(req):
	if req.method == 'POST':
		username=req.POST['username']
		password=req.POST['password']
		number=req.POST['number']
		if not (password and number and username):
			return render(req,'error.html',{'error':'学号、密码、房间号均不能为空','url':'/zhuce/'})
			#return HttpResponse('学号、密码、房间号均不能为空')
		patt='[0-9]{10}'
		patt=re.compile(patt,flags=0)
		match=patt.match(username)
		if match:
			try:
				a=User(username=username,password=password,number=number)
				a.save()
				flag=1
			except:
				return render(req, 'error.html', {'error':'该账户已被注册','url':'/zhuce/'})
				#return HttpResponse('该账户已被注册')
		else:
			return render(req, 'error.html', {'error': '学号格式输入错误，请重新输入','url':'/zhuce/'})
			#return HttpResponse('学号输入不正确，请重新输入')
		return render(req,'login.html',{'flag':flag})
	else:
		flag=0
	return render(req,'/zhuce/')
