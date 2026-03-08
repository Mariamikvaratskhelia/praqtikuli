from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentListCreateAPIView,
    RecommendationRequestDetailAPIView,
    ProfessorListCreateAPIView,
    SkillViewSet,
    RecommendationRequestListCreateAPIView,
    RecommendationLetterViewSet,
)

router = DefaultRouter()
router.register('skills', SkillViewSet, basename='skills')
router.register('letters', RecommendationLetterViewSet)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('professors/', ProfessorListCreateAPIView.as_view()),
    path('requests/', RecommendationRequestListCreateAPIView.as_view()),
    path('requests/<int:pk>/', RecommendationRequestDetailAPIView.as_view()),
    path('', include(router.urls)),
]