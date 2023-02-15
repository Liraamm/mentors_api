from django.contrib import admin

from .models import Category, Mentor, CategoryItem

admin.site.register(Category)
admin.site.register(Mentor)
admin.site.register(CategoryItem)