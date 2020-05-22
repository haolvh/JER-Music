from django.db import models


# Create your models here.
class Clist(models.Model):
    # 收藏歌单
    music_name = models.CharField(max_length=30)

    user_name = models.CharField(max_length=12)

    singer = models.CharField(max_length=20)

    time = models.CharField(max_length=20)
