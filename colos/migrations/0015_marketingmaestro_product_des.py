# Generated by Django 3.1.7 on 2021-03-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colos', '0014_auto_20210326_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingmaestro',
            name='product_des',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]