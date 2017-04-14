# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dorm',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('devID', models.PositiveIntegerField()),
                ('devName', models.CharField(max_length=4)),
                ('devStatus', models.PositiveIntegerField()),
                ('roomName', models.PositiveIntegerField()),
                ('nRelays', models.PositiveIntegerField()),
                ('relay1', models.PositiveIntegerField()),
                ('relay2', models.PositiveIntegerField()),
                ('relay3', models.PositiveIntegerField()),
                ('relay4', models.PositiveIntegerField()),
                ('relay5', models.PositiveIntegerField()),
            ],
        ),
    ]
