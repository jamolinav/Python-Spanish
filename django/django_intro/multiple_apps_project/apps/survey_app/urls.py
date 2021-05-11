from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('survey', views.index),
    path('survey/result', views.create_user),
]