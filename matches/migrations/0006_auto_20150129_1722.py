# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_match_tournament'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', blank=True, to='matches.Player', null=True),
            preserve_default=True,
        ),
    ]
