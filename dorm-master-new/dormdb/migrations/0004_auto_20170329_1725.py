# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0003_auto_20170329_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='devName',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
