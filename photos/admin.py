from django.contrib import admin

from .models import Photo
# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'commentary']

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
