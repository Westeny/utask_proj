# Generated by Django 2.1.7 on 2019-03-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190317_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidicap',
            name='vidicap_model',
            field=models.CharField(choices=[('Vidicap Stream', '3'), ('Vidicap HD', '1'), ('Vidicap Mini', '2'), ('Vidicap Touch', '4')], max_length=15, verbose_name='Модель Vidicap'),
        ),
    ]
