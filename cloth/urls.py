from django.urls import path
from . import views

urlpatterns = [
    path('cloth/product_list/', views.ProductListView.as_view(), name='product_list'),
    path('cloth/products/men/', views.men_clothing, name='men_clothing'),
    path('cloth/products/women/', views.women_clothing, name='women_clothing'),
    path('cloth/products/kids/', views.kids_clothing, name='kids_clothing'),
    path('cloth/products/unisex/', views.unisex_clothing, name='unisex_clothing'),
    path('cloth/create_order/', views.create_order, name='create_order'),
    path('cloth/products_by_tag/<str:tag_name>/', views.products_by_tag, name='products_by_tag'),
]