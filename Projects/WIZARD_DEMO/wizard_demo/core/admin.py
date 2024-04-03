from django.contrib import admin

from .models import Business, Guest, Booking

# Register your models here.
admin.site.register(Business)
admin.site.register(Guest)
admin.site.register(Booking)