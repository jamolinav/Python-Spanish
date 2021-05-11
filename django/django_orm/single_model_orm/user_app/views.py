from django.shortcuts import render
from user_app.models import *

users.objects.all().order_by('first_name')