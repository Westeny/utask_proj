# Generated by Django 2.1.7 on 2019-03-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190317_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidicap',
            name='vidicap_model',
            field=models.CharField(choices=[('Vidicap HD', '1'), ('Vidicap Touch', '4'), ('Vidicap Mini', '2'), ('Vidicap Stream', '3')], max_length=15, verbose_name='Модель Vidicap'),
        ),
    ]
