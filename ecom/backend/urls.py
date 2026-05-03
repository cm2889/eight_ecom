from django.urls import path

from .import views

urlpatterns = [
    path('dashboard/', views.ecom_dashboard, name='dashboard'),

    path('product-main-category-list/', views.product_main_category_list_view, name='product_main_category_list'),
    path('add-product-main-category/', views.add_product_main_category_view, name='add_product_main_category'),
    path('product-main-category/<int:pk>/', views.product_main_category_detail_view, name='product_main_category_detail_view'),

    path('product-list/', views.product_list_view, name='product_list'),
    path('product-create/', views.add_product_view, name='add_new_product'),

]
