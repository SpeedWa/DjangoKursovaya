from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin


class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'stock', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['stock', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
