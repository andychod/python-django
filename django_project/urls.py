"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from mainsite import views

news_pattern = [
    path('', views.live_index),
    path('<int:tvno>/', views.live_index, name='tv-url'),
    path('entv/', views.live_entv),
    path('entv/<int:tvno>/', views.live_entv, name='entv-url'),
]

blog_pattern = [
    path('', views.blog_index),
    path('<int:pid>/<str:del_pass>', views.blog_index),
    path('list/', views.blog_listing),
    path('post/', views.blog_posting),
]

tangpoetry_patterns = [
    path('', views.tang_poetry),
    path('post/<slug:slug>', views.tang_poetry_showpost)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tangpoetry/', include(tangpoetry_patterns)),
    path('livenews/', include(news_pattern)),
    path('blog/', include(blog_pattern)),
]
