from django.contrib import admin

from .models import Category, Mentor, CategoryItem

admin.site.register(Category)
admin.site.register(CategoryItem)

from django.db.models import Avg
from .models import Category, Mentor
from review.models import Comment



class CommentInline(admin.TabularInline):
    model = Comment
    
class MentorAdmin(admin.ModelAdmin):
    list_filter = ['name', 'category']
    list_display = ['name', 'years'] 
    search_fields = ['name', 'description']
    inlines = [CommentInline]
    
    
admin.site.register(Mentor, MentorAdmin)


