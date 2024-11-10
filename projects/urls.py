from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ProjectImageListCreateView, ProjectImageDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:project_id>/images/', ProjectImageListCreateView.as_view(), name='projectimage-list-create'),
    path('projects/images/<int:pk>/', ProjectImageDetailView.as_view(), name='projectimage-detail'),
]
