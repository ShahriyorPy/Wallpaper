"""
URL configuration for FonRasm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from main.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Wallpaper API",
      default_version='v1',
      description="Wallpaper - o'rganish maqsadida qilingan API'lar to'plamlaridan tashkil topgan loyiha",
      # terms_of_service="https://www.google.com/policies/terms/", # --> kerak emas chunki allowany
      contact=openapi.Contact(email="Abdulhamidov Shahriyor. Email: abdulhamidovpy@gmail.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallpapers/',PhotosListAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('wallpaper/<int:pk>/', PhotoListAPIView.as_view()),
]

