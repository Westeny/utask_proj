from django.db import models
from django.contrib.auth.models import User
import json
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


    def complite(self):
        self.is_complete = True
        return

class Vidicap(models.Model):
    """модель для контроля отгрузок vidicap"""

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
        return


class Tenders(models.Model):
    """модель описывающая тендеры"""

    tender_number = models.CharField('Номер конкурса', max_length=150)
    tender_lot = models.CharField('Номер лота', max_length=50)
    budget = models.CharField('Тип бюджета', max_length=50)
    date_podacha = models.DateField(auto_now=False) #дата и время дедлайна для подачи предложения на конкус
    date_tender = models.DateField(auto_now=False) #дата и время проведения торгов
    buyer = models.CharField('Покупатель', max_length=150)
    customer = models.CharField('Заказчик', max_length=150)
    sum_offer = models.IntegerField('Сумма предложения', default=0)
    note = models.CharField('Примечание', max_length=2500)

    def __str__(self):
        return self.tender_number + ' ' + self.tender_lot



