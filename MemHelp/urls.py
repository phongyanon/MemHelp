"""MemHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from random_word import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>\d+)/random_word/$', views.random_word, name='random_word'),
    url(r'^(?P<num>\d+)/(?P<seq>\w+)/random_word/$', views.random_word, name='random_word'),
    url(r'^random_interval/$', views.random_interval, name='random_interval'),
    url(r'^random_num/$', views.random_num, name='random_num'),
    url(r'^show_major/$', views.show_major, name='show_major'),
    url(r'^add_word/$', views.add_word, name='add_word'),
]
