# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20150129_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='max_players',
            field=models.PositiveIntegerField(default=4, choices=[(4, b'Four'), (8, b'Eight'), (16, b'Sixteen')]),
            preserve_default=True,
        ),
    ]
