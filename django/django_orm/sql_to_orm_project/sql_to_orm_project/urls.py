"""sql_to_orm_project URL Configuration

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
from sql_to_orm_app import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('add', views.add_book),
    path('books', views.books),
    path('books/<int:id>', views.view_book),
    path('add_author', views.add_author),
    path('author/add', views.new_author),
    path('authors/<int:id>', views.view_author),
    path('add_book', views.add_book),
    path('register', views.register),
    path('register_user', views.register_user),
    path('login', views.login),
    path('logout', views.logout),
    path('checkEmail',views.checkEmail),
    path('<str:s>', views.index2),
]
