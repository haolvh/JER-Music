# Generated by Django 3.0.6 on 2020-05-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JEmoudel', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicintro',
            name='music_pic',
            field=models.CharField(default='https://y.gtimg.cn/mediastyle/music_v11/extra/default_300x300.jpg', max_length=100),
        ),
    ]
