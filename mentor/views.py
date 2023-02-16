from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters

from review.serializers import LikeSerializer
from review.models import Like
from .models import Category, Mentor, CategoryItem
from .serializers import CategorySerializer, MentorSerializer, CategoryItemSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MentorViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        author = request.user
        mentor = self.get_object()
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(mentor=mentor, author=author)
                like.delete()
    
                message = 'disliked'
            except Like.DoesNotExist:
                Like.objects.create(mentor=mentor, is_liked=True, author=author)
                message = 'liked'
            return Response(message, status=200)

class CategoryItemView(ModelViewSet):
    queryset = CategoryItem.objects.all()
    serializer_class = CategoryItemSerializer