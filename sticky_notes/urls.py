"""Top-level URL routes for the Sticky Notes project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notes.urls")),
]
