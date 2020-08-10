# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190529_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='totalDonated',
            field=models.IntegerField(default=0),
        ),
    ]
