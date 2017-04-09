# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dorm',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
