# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20171227_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nombre',
            field=models.CharField(max_length=100, null=True, default='efectivo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numeroempleado',
            field=models.CharField(max_length=20, null=True, default='0000'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numerotarjeta',
            field=models.CharField(max_length=20, null=True, default='00000000000000'),
        ),
    ]
