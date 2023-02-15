from rest_framework.serializers import ModelSerializer


from django.db.models import Avg
from .models import Category, Mentor, CategoryItem

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'
    
    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)
    #     representation['category'] = [{'name':i.name, 'last_name':i.last_name, 'category':i.category.title, 'description':i.description, 'years':i.years} for i in instance.mentor.all()]
    #     return representation

class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['likes_count'] = instance.likes.count()
        return representation

class CategoryItemSerializer(ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = '__all__'
        
