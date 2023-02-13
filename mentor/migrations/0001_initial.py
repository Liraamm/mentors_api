
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('years', models.IntegerField(verbose_name='Стаж')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='mentor.category', verbose_name='Категория')),
            ],
        ),
    ]
