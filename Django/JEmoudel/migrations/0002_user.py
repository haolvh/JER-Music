# Generated by Django 3.0.6 on 2020-05-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JEmoudel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_tel', models.CharField(max_length=11)),
                ('user_name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=12)),
            ],
        ),
    ]
