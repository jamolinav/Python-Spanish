from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('login', views.login),
    path('users', views.users),
    path('user/new_user', views.new),
    path('user/<int:id>', views.show),
    path('user/<int:id>/edit', views.edit),
    path('user/<int:id>/destroy', views.delete),
    path('user/create', views.insert),
]