# Generated by Django 5.1.1 on 2024-11-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pontodecoleta_coordenadax_pontodecoleta_coordenaday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontodecoleta',
            name='coordenadaX',
            field=models.FloatField(default='Default X', max_length=255, verbose_name='coordenada X no mapa'),
        ),
        migrations.AlterField(
            model_name='pontodecoleta',
            name='coordenadaY',
            field=models.FloatField(default='Default Y', max_length=255, verbose_name='coordenada Y no mapa'),
        ),
    ]
