from django.contrib import admin
from products.models import Product
from branches.models import Branch

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'calories']
    search_fields = ('name',)

@admin.register(Branch)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'work_hours', 'special']
    search_fields = ('name',)