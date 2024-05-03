# Generated by Django 5.0.4 on 2024-05-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_remove_instrumentoaire_instrumento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumentoaire',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='instrumentoviento',
            name='nombre',
        ),
        migrations.AddField(
            model_name='instrumentoaire',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción'),
        ),
        migrations.AddField(
            model_name='instrumentoviento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción'),
        ),
    ]