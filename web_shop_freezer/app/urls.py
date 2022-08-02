from django.urls import path
from . import views

urlpatterns = [
    path('', views.freezers, name='freezers'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('price_up/', views.price_up, name='price_up')
]
