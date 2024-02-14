from django.urls import path
from Base.views import home_page, about_page, privacy_page, license_page


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('privacy/', privacy_page, name='privacy'),
    path('license/', license_page, name='license')
]
