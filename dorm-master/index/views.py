# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect

from query.forms import DevRoomForm

# Create your views here.


def index(request):
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
        'cards': cards})

def denglu(request):
	return render(request,'login.html')
	
def zhuce(request):
	return render(request,'regist.html')