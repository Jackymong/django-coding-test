from email import message
from itertools import product
from multiprocessing import context
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request,"store/index.html")

def Collections(request):
    category = Category.objects.filter(status=0)
    contex={'category':category}
    return render(request,"store/Collections.html",contex)

# for find the category wise product
def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products,'category':category}
        return render(request,'store/products/index.html',context) 
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug).first
            context={'products':products}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request,'store/products/view.html',context)
