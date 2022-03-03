from django.http import Http404
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phones = phone_objects.order_by(SORT_MAP[sort])
    else:
        phones = phone_objects

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone_object = Phone.objects.get(slug=slug)
    except:
        raise Http404("Error")
    context = {
        'phone': phone_object,
    }
    return render(request, template, context)

