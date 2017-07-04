# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='b',
            field=models.TextField(null=True),
        ),
    ]
