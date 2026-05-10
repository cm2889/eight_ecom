from django.urls import path

from .import views

urlpatterns = [
    path('dashboard/', views.ecom_dashboard, name='dashboard'),

    path('product-main-category-list/', views.product_main_category_list_view, name='product_main_category_list'),
    path('add-product-main-category/', views.add_product_main_category_view, name='add_product_main_category'),
    path('product-main-category/<int:pk>/', views.product_main_category_detail_view, name='product_main_category_detail_view'),

    path('product-list/', views.product_list_view, name='product_list'),
    path('product-create/', views.add_product_view, name='add_new_product'),
    path('', views.home, name='home'),
    path('products/', views.product_web_list, name='product_web_list'),
     path('products/<slug:product_slug>/', views.products_details, name='products_details'),


     #Authentication
    path('register/', views.register, name='register'),
    path('request-otp/', views.request_otp_view, name='request_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),

    #ajax
    path('add-or-update-cart/', views.add_or_update_cart, name='add_or_update_cart'),

    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]
