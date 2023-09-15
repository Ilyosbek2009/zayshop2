from django.contrib import admin

from apps.models import Category, Product


# from apps.urls import urlpatterns


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'slug')
    readonly_fields = ('slug',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'price', 'short_desc', 'review', 'brand', 'color', 'slug')
    readonly_fields = ('slug',)
