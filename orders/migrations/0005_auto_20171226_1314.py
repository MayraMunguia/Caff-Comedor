# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171222_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nombre',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='numeroempleado',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='numerotarjeta',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
