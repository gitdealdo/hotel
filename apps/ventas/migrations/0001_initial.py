# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('pax', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('importe', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Consumo',
                'verbose_name_plural': 'Consumos',
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pago', models.CharField(blank=True, choices=[(b'EFECTIVO', b'Efectivo'), (b'TARJETA', b'Tarjeta')], default=b'EFECTIVO', max_length=8)),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Consumo')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Habitacion')),
            ],
        ),
    ]
