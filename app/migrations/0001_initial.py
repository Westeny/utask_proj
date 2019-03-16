# Generated by Django 2.1.4 on 2019-03-15 13:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=150, verbose_name='Task')),
                ('deadline_date', models.DateField()),
                ('tags', models.CharField(max_length=150, verbose_name='Tags')),
                ('note', models.CharField(max_length=5000, verbose_name='Note')),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
