# Generated by Django 3.1.7 on 2021-03-10 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colos', '0007_auto_20210309_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_img',
        ),
    ]
