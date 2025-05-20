"""
URL configuration for backend project.

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
from django.urls import path
from api.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('api/v1/authors/', AuthorListView.as_view(), name='author-list'),
    path('api/v1/authors/<int:id>/', AuthorDetailView.as_view(), name='author-detail'),
    
    path('api/v1/genres/', GenreListView.as_view(), name='genre-list'),
    path('api/v1/genres/<int:id>/', GenreDetailView.as_view(), name='genre-detail'),
    
    path('api/v1/books/', BookListView.as_view(), name='book-list'),
    path('api/v1/books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
]
