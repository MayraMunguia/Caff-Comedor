# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20171222_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='NumeroEmpleado',
            new_name='numeroempleado',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='NumeroTarjeta',
            new_name='numerotarjeta',
        ),
    ]
