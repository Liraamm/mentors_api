# Generated by Django 4.1.6 on 2023-02-15 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('payment', models.CharField(choices=[('По карте', 'По карте'), ('Наличными', 'Наличными')], max_length=30, verbose_name='Оплата')),
                ('service', models.CharField(choices=[('Первый урок', 'Первый урок'), ('Второй урок', 'Второй урок'), ('Третий урок', 'Третий урок')], max_length=20, verbose_name='Уроки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mentor.mentor')),
            ],
        ),
    ]