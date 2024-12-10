from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products=product.objects.order_by('-priority')[:4]
    latest_products=product.objects.order_by('-id')[:4]
    context={
        featured_products:featured_products,
        latest_products:latest_products
    }
    return render(request,'index.html',context)

def list_products(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    
    product_list=product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    
    return render(request,'products.html',context)

def detail_products(request,pd):
    products=products.objects.get(pd=pd)
    context={'products':products}
        
    return render(request,'product_detail.html',context)