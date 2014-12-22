# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
