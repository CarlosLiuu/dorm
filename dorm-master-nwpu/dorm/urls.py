"""dorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from index import views as index_views
from query import views as query_views
from users import views as users_views
#from weixin import views as weixin_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_views.index, name='index'),
    url(r'^index/', index_views.index, name='index'),
    url(r'^queryall/', query_views.queryall, name='queryall'),
    url(r'^deletedata/', query_views.deletedata, name='deletedata'),
	url(r'^denglu/',index_views.denglu,name='denglu'),
	url(r'^zhuce/',index_views.zhuce,name='zhuce'),
	url(r'^regist',users_views.register,name='regist'),
	url(r'^login',users_views.login,name='login'),
    url(r'^ao',users_views.ao,name='ao'),
    #url(r'^weixin',weixin_views.wechat,name='weixin'),
]
