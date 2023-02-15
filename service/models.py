from django.db import models

from django.contrib.auth import get_user_model

from mentor.models import Mentor

User = get_user_model()

class Application(models.Model):
    author = models.ForeignKey(User, related_name= 'applications',on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='orders')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    payments = [
        ('По карте', 'По карте'),
        ('Наличными', 'Наличными'),
    ]
    payment = models.CharField(max_length=30, choices=payments, verbose_name='Оплата')
    services = [
        ('Ознакомительный урок', 'Ознакомительный урок'),
        ('Урок закрепления', 'Урок закрепления'),
        ('Урок практики', 'Урок практики'),
    ]
    service = models.CharField(max_length=69, choices=services, verbose_name='Уроки')

    def __str__(self) -> str:
        return f'Application id: {self.pk}'
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'