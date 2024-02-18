from django.urls import path
from House.views import listing


urlpatterns = [
    path('listing/', listing, name='listing')
]
