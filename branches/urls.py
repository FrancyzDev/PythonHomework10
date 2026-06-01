from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('<int:branch_id>/', views.BranchesDetailView.as_view(), name='branches_detail'),
]