from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'url', 'user', 'created')
    list_display_links = ('title', 'slug')


admin.site.register(Image, ImageAdmin)
