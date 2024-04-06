from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'slug', 'price', 'available', 'created_at')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}