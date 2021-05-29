from django.contrib import admin
from .models import Category, Tag, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ['pk', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ['pk', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')
    search_fields = ['pk', 'tags', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
