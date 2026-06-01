from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', include('news.urls')),
    path('branches/', include('branches.urls')),
    path('products/', include('products.urls'))
]

handler404 = 'core.views.custom_404'