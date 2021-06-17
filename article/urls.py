
from django.contrib import admin
from django.urls import path
from .import views

# Create your models here.

urlpatterns = [
    path('', views.article_list),

]
