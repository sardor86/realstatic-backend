from django.http import HttpResponse
from django.shortcuts import render


def home_page(request) -> HttpResponse:
    return render(request, 'templates/base/index.html')
