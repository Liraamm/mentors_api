from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Category, Mentor
from .serializers import CategorySerializer, MentorSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MentorViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer