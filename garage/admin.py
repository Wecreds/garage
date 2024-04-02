from django.contrib import admin

from .models import Accessory, Category, Color

admin.site.register(Accessory)
admin.site.register(Category)
admin.site.register(Color)