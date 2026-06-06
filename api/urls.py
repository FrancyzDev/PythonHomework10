from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),

    path('branches/', views.branches_list),
    path('branches/<int:pk>/', views.branch_detail),
]