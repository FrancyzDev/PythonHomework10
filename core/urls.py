from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', include('news.urls')),
    path('branches/', include('branches.urls')),
    path('products/', include('products.urls')),
    path('api/', include('api.urls')),
]