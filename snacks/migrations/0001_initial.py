# Generated by Django 2.2.1 on 2019-06-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('v_tipo', models.CharField(max_length=50)),
                ('v_nombre', models.CharField(max_length=50)),
                ('tx_descripcion', models.TextField()),
                ('i_precio', models.IntegerField()),
                ('i_puntosofrecidos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'snack',
                'managed': True,
            },
        ),
    ]
