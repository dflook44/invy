# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cost',
            field=models.DecimalField(max_digits=20, decimal_places=2, default=0),
            preserve_default=False,
        ),
    ]
