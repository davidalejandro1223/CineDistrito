# Generated by Django 2.2.1 on 2019-06-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20190630_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='i_telefono',
            field=models.BigIntegerField(verbose_name='Telefono'),
        ),
    ]
