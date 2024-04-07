from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.item_list, name = 'item_list'),
    path('drf/', views.item_list_serialized, name = 'item_list_serialized'),
    path('<int:pk>/', views.item_detail_view, name = 'item_detail_view'),
]
