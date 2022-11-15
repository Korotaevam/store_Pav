from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = {
        'title': 'Store',
        'header': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Store - Catalog',
        'header': 'Catalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),

    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать',
        'username': 'ivan ivanovich',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'promotion': True,
        'products_of_promotion':
            [{'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},

             ]

    }
    return render(request, 'products/test-context.html', context)

# print(1111111, Product.objects.filter(quantity__gt=5))
