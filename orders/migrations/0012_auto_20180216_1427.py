# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20180131_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nomina',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
        migrations.AddField(
            model_name='order',
            name='razon_social',
            field=models.CharField(max_length=50, blank=True, null=True, default='-'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numeroempleado',
            field=models.CharField(max_length=20, blank=True, null=True, default='-'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numerotarjeta',
            field=models.CharField(max_length=20, blank=True, null=True, default='-'),
        ),
    ]
