from django.contrib import admin

from listings.models import Band

from listings.models import Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed', 'genre', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing,ListingAdmin)