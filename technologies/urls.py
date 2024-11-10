from django.urls import path
from .views import TechnologyListCreateView, TechnologyDetailView

urlpatterns = [
    path('technologies/', TechnologyListCreateView.as_view(), name='technology-list-create'),
    path('technologies/<int:pk>/', TechnologyDetailView.as_view(), name='technology-detail'),
]
