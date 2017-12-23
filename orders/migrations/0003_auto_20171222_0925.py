# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171222_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='numeroempleado',
            new_name='NumeroEmpleado',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='numerotarjeta',
            new_name='NumeroTarjeta',
        ),
    ]
