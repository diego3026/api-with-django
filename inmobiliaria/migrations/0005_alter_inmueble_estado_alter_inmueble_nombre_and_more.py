# Generated by Django 4.2.7 on 2023-11-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0004_alter_inmueble_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='estado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
