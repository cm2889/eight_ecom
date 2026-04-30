from django.urls import path

from .import views

urlpatterns = [
    path('dashboard/', views.ecom_dashboard, name='dashboard'),
]
