# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20180224_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(help_text='轮播图', upload_to='banner/', verbose_name='轮播图'),
        ),
    ]
