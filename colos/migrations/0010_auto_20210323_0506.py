# Generated by Django 3.1.6 on 2021-03-22 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colos', '0009_auto_20210323_0503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='highScore',
            new_name='colo_coins',
        ),
    ]