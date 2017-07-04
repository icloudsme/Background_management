# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170321_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='a',
        ),
        migrations.RemoveField(
            model_name='article',
            name='b',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
