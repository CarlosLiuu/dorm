# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0007_auto_20170329_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
