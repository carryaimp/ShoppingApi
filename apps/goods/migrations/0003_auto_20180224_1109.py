# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180224_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='good_desc',
            new_name='goods_desc',
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, help_text='商品类目', null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(blank=True, help_text='商品类目', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]