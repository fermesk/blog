
from django.contrib import admin 
from django.urls import include, path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', views.about_us),
    path('homepage/', views.homepage),
    path('article', include('article.urls')),

]
