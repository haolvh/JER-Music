from django.urls import path

from JEmoudel.views import play, download, login, register, test

urlpatterns = [

    path('song/post', play),

    path('song/download', download),

    path('user/login', login),

    path('user/register', register),

    path('test', test),


]
