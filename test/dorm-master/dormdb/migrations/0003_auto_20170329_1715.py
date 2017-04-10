# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0002_dorm_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='devID',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='devStatus',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='nRelays',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='relay1',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='relay2',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='relay3',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='relay4',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='relay5',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='roomName',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
