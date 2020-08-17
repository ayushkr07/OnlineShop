from django.shortcuts import render

from .models import Product,ProductImages

def index(request):
    products=Product.objects.all()
    context={
        'products': products
    }
    return render(request,'index.html',context)


def productDetail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
