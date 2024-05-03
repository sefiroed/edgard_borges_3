# Generated by Django 5.0.4 on 2024-05-02 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_rename_instrumentoviento_instrumentocuerdas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='instrumentoaire',
        ),
        migrations.RemoveField(
            model_name='instrumento',
            name='instrumentocuerdas',
        ),
        migrations.AddField(
            model_name='instrumento',
            name='instrumentoaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.instrumentoaire'),
        ),
        migrations.AddField(
            model_name='instrumento',
            name='instrumentocuerdas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.instrumentocuerdas'),
        ),
    ]
