# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms  
from users.models import User
from django.http import HttpResponse,HttpResponseRedirect
from users.form import LoginForm
# Create your views here.
	
def login(req):  
    if req.method == 'POST':  
        uf = LoginForm(req.POST)  
        if uf.is_valid():  
            username = uf.cleaned_data['username']  
            password = uf.cleaned_data['password']  
            user = User.objects.filter(username__exact = username,password__exact = password)  
            if user:  
                req.session['username'] = username  
                return HttpResponseRedirect('/index')  
            else:  
                err = 'incorrect username or pwd,please input again.'  
                return render(req,'register.html',{'err':err})  
    else:  
        uf = LoginForm()  
    return render(req,'login.html',{'uf':uf})
	
def register(req):
	if req.method == 'POST':
		uf=LoginForm(req.POST)
		if uf.is_valid():
			username=uf.cleaned_data['username']
			password=uf.cleaned_data['password']
			number=uf.cleaned_data['num']
			User.object.create(username=username,password=password,number=number)
			User.save()
			return render(req,'login.html')
	else:
		uf=LoginForm()
	return render(req,'register.html')
