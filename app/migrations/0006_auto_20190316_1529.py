# Generated by Django 2.1.7 on 2019-03-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190316_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidicap',
            name='vidicap_model',
            field=models.CharField(choices=[('Vidicap Mini', '2'), ('Vidicap HD', '1'), ('Vidicap Stream', '3'), ('Vidicap Touch', '4')], max_length=15, verbose_name='Модель Vidicap'),
        ),
    ]
