from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, MentorViewSet

router = DefaultRouter()
router.register('mentors', MentorViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]