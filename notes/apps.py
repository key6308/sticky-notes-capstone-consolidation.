"""Configuration for the notes Django application."""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Set the default database key type and app name."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"
