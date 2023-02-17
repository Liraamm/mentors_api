from rest_framework.serializers import ModelSerializer

from .models import Category, Mentor

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['category'] = [{'name':i.name, 'last_name':i.last_name, 'category':i.category.title, 'description':i.description, 'years':i.years} for i in instance.mentor.all()]
        return representation

class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
    


