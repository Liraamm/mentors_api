from rest_framework.serializers import ModelSerializer

from .models import Category, Mentor

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'


class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'