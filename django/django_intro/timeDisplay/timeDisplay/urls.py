"""timeDisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app_random_word import views as random_word_views
from app_time_display import views as time_display_views

urlpatterns = [
    path('', time_display_views.index),
    path('time_display', time_display_views.time_display),
    path('some_route', time_display_views.some_function),
    path('random_word', random_word_views.random_word),
    path('reset', random_word_views.reset)
]
