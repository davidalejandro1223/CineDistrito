# Generated by Django 2.2.1 on 2019-07-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20190711_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='t_inicioreserva',
            field=models.TimeField(auto_now=True),
        ),
    ]
