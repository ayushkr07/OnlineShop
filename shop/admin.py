from django.contrib import admin

from shop.models.product import ProductImages, Product


class ProductImageModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    inlines = [ProductImageModel]


admin.site.register(Product, ProductModel)
