from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    """модель задач"""
    user = models.ForeignKey(User, null=True, on_delete=None)
    task_name = models.CharField('Task', max_length=150)
    deadline_date = models.DateField()
    tags = models.CharField('Tags', max_length=150)
    note = models.CharField('Note', max_length=5000)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


class Vidicap(models.Model):
    """модель для контроля отгрузок и установок vidicaps"""

    vidicap_type = {
        ('Vidicap HD', '1'),
        ('Vidicap Mini', '2'),
        ('Vidicap Stream', '3'),
        ('Vidicap Touch', '4')
    }

    vidicap_model = models.CharField('Модель Vidicap', max_length=15, choices=vidicap_type)
    sell_date = models.DateField()
    set_up_place = models.CharField('Место устрановки', max_length=300)
    note = models.CharField(max_length=1500)
    set_up_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.vidicap_model + ' ' + self.set_up_place

    def complite(self):
        self.set_up_complete = True


#class Tenders(models.Model):
    """модель описывающая тендеры"""






