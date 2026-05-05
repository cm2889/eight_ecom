from django.contrib import admin

from backend.models import Product, ProductMainCategory, ProductSubCategory,EmailOTP

# Register your models here.
admin.site.register(ProductMainCategory)

admin.site.register(Product)

admin.site.register(ProductSubCategory)

admin.site.register(EmailOTP)