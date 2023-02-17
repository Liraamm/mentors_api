from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=40, unique=True)
    slug = models.SlugField(max_length=40, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Mentor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    category = models.ManyToManyField(Category, through='CategoryItem')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    years = models.IntegerField(verbose_name='Стаж')

    def __str__(self) -> str:
        return f'Ментор {self.name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'
 


class CategoryItem(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='item')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_item')

    # def __str__(self) -> str:
    #     return self.category

    class Meta:
        verbose_name = 'Элемент категории'
        verbose_name_plural = 'Элементы категории'
