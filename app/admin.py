from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Colour, Brand, Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_filter = ('name',)
    search_fields = ('id', 'name')

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='75'> ")

class ColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')



class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'colour', 'brand', 'price', 'price_types', 'get_image')
    list_filter = ('brand', 'colour')
    search_fields = ('id', 'model', 'brand')

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='75'> ")

admin.site.register(Brand, BrandAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Car, CarAdmin)
