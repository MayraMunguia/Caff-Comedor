# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20171227_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='empleado',
        ),
        migrations.AddField(
            model_name='order',
            name='nombre',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='numeroempleado',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='numerotarjeta',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
