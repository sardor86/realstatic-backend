from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from House.models import House, HouseImages


def listing(request: WSGIRequest):
    products_list = House.objects.all()
    paginator = Paginator(products_list, 6)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context: dict = {
        'products': [{
            'house': item,
            'image': HouseImages.objects.filter(house=item).first()
        } for item in products],
        'products_list': products
    }

    return render(request, 'templates/house/listing.html', context)
