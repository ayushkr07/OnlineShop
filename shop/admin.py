from django.contrib import admin
from django.utils.html import  format_html

from shop.models.product import ProductImages, Product


class ProductImageModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_description','get_price','get_discount','get_sale_price','file','thumbnail']
    inlines = [ProductImageModel]

    def get_description(self,obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15]}...</span>')

    def get_price(self,object):
        return '₹ '+str(object.price)

    def get_discount(self,object):
        return str(object.discount)+'%'

    def get_sale_price(self,obj):
        return '₹ '+str(obj.price-(obj.price*obj.discount)/100)

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"

admin.site.register(Product, ProductModel)
