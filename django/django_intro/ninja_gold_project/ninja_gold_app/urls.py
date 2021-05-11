from django.urls import path
from . import views

#app_name = 'ninja_gold'
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('process_money', views.process_money),
    path('process_money/<str:form>', views.process_money),
]