from django.http import HttpResponse
from django.shortcuts import render


def home_page(request) -> HttpResponse:
    return render(request, 'templates/base/index.html')


def about_page(request) -> HttpResponse:
    return render(request, 'templates/base/about.html')


def privacy_page(request) -> HttpResponse:
    return render(request, 'templates/base/privacy.html')


def license_page(request) -> HttpResponse:
    return render(request, 'templates/base/license.html')
