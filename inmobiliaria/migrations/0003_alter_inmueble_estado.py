# Generated by Django 4.2.7 on 2023-11-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0002_remove_inmueble_cantidaddehabitantes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]