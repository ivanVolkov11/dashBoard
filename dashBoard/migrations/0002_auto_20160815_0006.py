# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('is done', 'done'), ('in work', 'in work')], max_length=10),
        ),
    ]
