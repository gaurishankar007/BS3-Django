from django.shortcuts import render
from .models import Product
from .forms import ProductForm, PersonForm
# Create your views here.


def index(request):
    items = Product.objects.all()
    context = {
        'products': items
    }
    return render(request, 'Product/django_web.html', context)


def post_product_data(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'Product/postProduct.html', context)


def ger_form(request):
    form = PersonForm()
    context = {'form': form}
    return render(request, 'Product/PersonForm.html', context)