from django.contrib import admin
from django.urls import path

# For Media file Configuraton
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.clients, name='clients'),
    path('recorded/', views.recorded, name='recorded'),
    path('live/', views.live, name='live'),
    path('start_live/<str:ip>/', views.start_live, name='start_live'),
    path('stop_live/<str:ip>/', views.stop_live, name='stop_live'),
    path('accounts/login/', views.login, name='login'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
