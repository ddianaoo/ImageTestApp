from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_photo', 'uploaded_at']
    list_display_links = ['id', 'title', 'get_photo']
    search_fields = ['title',]

    def get_photo(self, obj):
        if obj.image:
            print(obj.image.url)
            return mark_safe(f'<img src="{obj.image.url}" width="85">')
        else:
            # return mark_safe(f'<img src="https://picsum.photos/id/1060/75/40/?blur=2">')
            return mark_safe('-')

    get_photo.short_description = 'Small image'


admin.site.register(Image, ImageAdmin)