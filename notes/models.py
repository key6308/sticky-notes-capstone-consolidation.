"""Database models for the sticky notes application."""

from django.db import models


class StickyNote(models.Model):
    """Store a sticky note with a title and text content."""

    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        """Return the note title for readable display in Django admin."""
        return self.title
