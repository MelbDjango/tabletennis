# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20150129_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'get_latest_by': 'created'},
        ),
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(to='matches.Player', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
    ]
