#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:LvHao
@license: Apache Licence 
@file: urls.py.py 
@time: 2020/05/24
@site:  
@software: PyCharm 
"""

from django.urls import path

from JERMusic.views import collect, show_song, search, login, register, play, download, show_collection

urlpatterns = [

    path('user', show_collection),

    path('collect', collect),

    path('login', login),

    path('register', register),

    path('show_song', show_song),

    path('search', search),

    path('play', play),

    path('download', download),
]
