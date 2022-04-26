from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name','created']