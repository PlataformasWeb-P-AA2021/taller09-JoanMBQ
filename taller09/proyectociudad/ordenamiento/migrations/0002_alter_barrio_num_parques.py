# Generated by Django 3.2.4 on 2021-06-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='num_parques',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], verbose_name='Numero de parques'),
        ),
    ]
