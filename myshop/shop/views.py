from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from myshop.settings import LANGUAGE_CODE
from .models import Category, Product


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        print(language)
        category = get_object_or_404(Category,
                                     translations__slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})