"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.messages import api
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


# Customize the admin site header
admin.site.site_header = "Arif's Portfolio"
admin.site.site_title = "My Awesome Portfolio"
admin.site.index_title = "Hey Arif! Welcome back."
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls"), name="accounts"),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("technologies/api/", include("technologies.urls")),
    path("projects/api/", include("projects.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        # YOUR PATTERNS
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

