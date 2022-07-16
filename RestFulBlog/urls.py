"""RestFulBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls, name='Django-Admin'),
    path('api/v1/blog/', include('api.urls'), name='Version 1 Blog APIs'),
    path('auth/', include('user.urls'), name='Authentication'),
    path('api-auth/', include('rest_framework.urls'), name='DRF Authentication'),
    path('', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='API Documentation'),
path('openapi', get_schema_view(
            title="Blog Restful APIs",
            description="Interactive blog APIs sub-system written in Django Framework!",
            version="1.0.0"
        ), name='openapi-schema'),
]
