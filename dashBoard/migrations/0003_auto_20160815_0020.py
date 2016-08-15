# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0002_auto_20160815_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='dashBoard.TaskList'),
        ),
    ]
