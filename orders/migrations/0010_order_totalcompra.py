# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20171228_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalcompra',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
