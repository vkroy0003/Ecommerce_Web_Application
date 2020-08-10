# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190528_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default=b'', max_length=70)),
                ('phone', models.CharField(default=b'', max_length=70)),
                ('desc', models.CharField(default=b'', max_length=500)),
            ],
        ),
    ]
