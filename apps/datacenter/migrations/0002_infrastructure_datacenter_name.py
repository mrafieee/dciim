# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructure',
            name='datacenter_name',
            field=models.CharField(default=b'ITRC Datacenter', max_length=100),
        ),
    ]
