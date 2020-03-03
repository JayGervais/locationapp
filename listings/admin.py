from django.contrib import admin
from .models import Listing


# customize admin area
admin.site.register(Listing)
