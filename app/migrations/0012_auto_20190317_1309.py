# Generated by Django 2.1.7 on 2019-03-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190317_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidicap',
            name='vidicap_model',
            field=models.CharField(choices=[('Vidicap Stream', '3'), ('Vidicap HD', '1'), ('Vidicap Touch', '4'), ('Vidicap Mini', '2')], max_length=15, verbose_name='Модель Vidicap'),
        ),
    ]