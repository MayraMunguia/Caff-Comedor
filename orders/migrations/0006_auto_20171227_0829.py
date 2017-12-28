# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20171226_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100, blank=True, null=True)),
                ('numerotarjeta', models.CharField(max_length=20, blank=True, null=True)),
                ('numeroempleado', models.CharField(max_length=20, blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='order',
            name='numeroempleado',
        ),
        migrations.RemoveField(
            model_name='order',
            name='numerotarjeta',
        ),
        migrations.AddField(
            model_name='order',
            name='empleado',
            field=models.ForeignKey(default=1234123, to='orders.Empleado'),
            preserve_default=False,
        ),
    ]
