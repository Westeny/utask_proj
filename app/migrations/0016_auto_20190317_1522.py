# Generated by Django 2.1.7 on 2019-03-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190317_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidicap',
            name='vidicap_model',
            field=models.CharField(choices=[('Vidicap Mini', '2'), ('Vidicap Touch', '4'), ('Vidicap Stream', '3'), ('Vidicap HD', '1')], max_length=15, verbose_name='Модель Vidicap'),
        ),
    ]