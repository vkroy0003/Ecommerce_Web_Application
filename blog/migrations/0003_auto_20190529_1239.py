# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190529_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
