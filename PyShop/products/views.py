from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New products page')
# bootstrap for css
# https://getbootstrap.com/docs/4.0/getting-started/introduction/