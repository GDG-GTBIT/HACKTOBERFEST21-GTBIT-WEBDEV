from django.urls import path
from items import views

urlpatterns = [
    path('', views.all_items, name = 'all_items'),
    path('<str:product_id>/', views.single_item, name = 'single_item')
]
