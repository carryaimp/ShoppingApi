# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='singer_mobile',
            new_name='signer_mobile',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='singer_name',
            new_name='signer_name',
        ),
    ]