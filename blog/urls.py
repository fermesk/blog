
from django.contrib import admin 
from django.urls import include, path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', views.about_us),
    path('homepage/', views.homepage),
    path('article/', include('article.urls')),
    path('account/', include('account.urls')),


]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)