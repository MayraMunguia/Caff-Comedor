# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180216_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='numerotarjeta',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
