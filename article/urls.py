
from django.contrib import admin
from django.urls import path
from .import views

# Create your models here.

urlpatterns = [
    path('', views.article_list,name="article"),
    path('create/', views.create,name="create"),
    path('<slug>/', views.article_detail,name="article_detail"),

]
