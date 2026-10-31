"""Register sticky note data with the Django administration site."""

from django.contrib import admin

from .models import StickyNote

admin.site.register(StickyNote)
