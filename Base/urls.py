from django.urls import path
from Base.views import home_page


urlpatterns = [
    path('', home_page, name='home')
]
