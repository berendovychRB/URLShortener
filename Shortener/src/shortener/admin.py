from django.contrib import admin

# Register your models here.
from .models import KirrURL


class KirrURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'shortcode')
    fields = ('id', 'url', 'shortcode')


admin.site.register(KirrURL, KirrURLAdmin)