# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20180326_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
        migrations.AddField(
            model_name='order',
            name='correo',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
        migrations.AddField(
            model_name='order',
            name='segmento',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
        migrations.AddField(
            model_name='order',
            name='sucursal',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
    ]
