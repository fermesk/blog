
from django.contrib import admin 
from django.urls import include, path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', views.about_us),
    path('homepage/', views.homepage),
    path('article', include('article.urls')),

]
urlpatterns+=staticfiles_urlpatterns()