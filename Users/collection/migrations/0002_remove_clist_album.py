# Generated by Django 3.0.6 on 2020-05-21 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clist',
            name='album',
        ),
    ]