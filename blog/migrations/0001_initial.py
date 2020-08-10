# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default=b'', max_length=500)),
                ('chead0', models.CharField(default=b'', max_length=5000)),
                ('head1', models.CharField(default=b'', max_length=500)),
                ('chead1', models.CharField(default=b'', max_length=5000)),
                ('head2', models.CharField(default=b'', max_length=500)),
                ('chead2', models.CharField(default=b'', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default=b'', upload_to=b'shop/images')),
            ],
        ),
    ]
