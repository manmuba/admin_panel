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
    path('users/add_clients/', views.add_clients, name='add_clients'),
    path('recorded/', views.recorded, name='recorded'),
    path('get_live_data/', views.get_live_data, name='get_live_data'),
    path('live/', views.live, name='live'),
    path('delete_client/<str:email>/', views.delete_client, name='delete_client'),
    path('start_live/<str:ip>/', views.start_live, name='start_live'),
    path('stop_live/<str:ip>/', views.stop_live, name='stop_live'),
    path('accounts/login/', views.login, name='login'),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
