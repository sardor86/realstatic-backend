from django.contrib import admin
from House.models import House, HouseImages


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size', 'address')
    search_fields = ('title', 'price', 'size', 'address')


@admin.register(HouseImages)
class HouseImagesAdmin(admin.ModelAdmin):
    list_display = ['house']
