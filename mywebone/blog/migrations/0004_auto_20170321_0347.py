# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 3, 47, 57, 961336), auto_now=True),
            preserve_default=False,
        ),
    ]
