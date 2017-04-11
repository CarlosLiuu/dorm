# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from query.forms import DevRoomForm


class LoginForm(forms.Form):
	username=forms.IntegerField(label='username')
	password=forms.CharField(label='password',widget=forms.PasswordInput())
	number=forms.IntegerField(label='number')
class sub:
	def __init__(self,username):
		self.username=username
	def index(self,request):
		form = DevRoomForm()
		card1 = {'title': '开灯',
				 'color': 'blue',
				 'content': 'Turn on your light.',
				 'action1': {'url': '/queryall/', 'name': '查询'},
				 'action2': {'url': '/queryall/', 'name': '查询'}}
		card2 = {'title': '开灯',
				 'color': 'green',
				 'content': 'Turn on your light.',
				 'action1': {'url': '/queryall/', 'name': '查询'},
				 'action2': {'url': '/queryall/', 'name': ''}}
		cards = []
		cards.append(card1)
		cards.append(card2)
		formData = {
			'title': '查询',
			'color': 'white',
			'content': 'Query all data from database.',
		}
		return render(request, 'index.html', {
			'form': form,
			'formData': formData,
			'cards': cards,
			'username':self.username})
