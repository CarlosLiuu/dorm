# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0005_auto_20170329_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
