# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190529_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
