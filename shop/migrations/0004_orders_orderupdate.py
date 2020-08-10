# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default=b'', max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(serialize=False, primary_key=True)),
                ('order_id', models.IntegerField(default=b'')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
