from django.contrib import admin
from django.db import models


# Create your models here.


class MusicIntro(models.Model):
    # 歌曲ID  主键唯一
    music_id = models.AutoField(primary_key=True)

    # 歌曲名称
    music_name = models.CharField(max_length=50)

    # 歌曲播放的爬虫连接
    music_URL = models.CharField(max_length=500)

    # 歌曲的演唱者
    music_singer = models.CharField(max_length=20)

    # 歌曲时长
    music_time = models.CharField(max_length=20)

    # 歌曲图片的信息
    music_pic = models.CharField(max_length=100, default="https://y.gtimg.cn/mediastyle/music_v11/extra"
                                                         "/default_300x300.jpg")


admin.site.register(MusicIntro)


class User(models.Model):
    # 用户手机号
    user_tel = models.CharField(max_length=11)

    # 用户名  作为主键  唯一
    user_name = models.CharField(max_length=12, primary_key=True)

    # 用户密码
    user_password = models.CharField(max_length=12)


admin.site.register(User)


class Clist(models.Model):
    # 收藏歌单
    music_name = models.CharField(max_length=30)

    user_name = models.CharField(max_length=12)

    singer = models.CharField(max_length=20)

    time = models.CharField(max_length=20)


admin.site.register(Clist)

