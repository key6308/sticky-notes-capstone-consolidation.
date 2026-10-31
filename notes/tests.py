"""Tests for the main sticky note features."""

from django.test import TestCase
from django.urls import reverse

from .models import StickyNote


class StickyNoteTests(TestCase):
    """Check that users can view and manage notes."""

    def setUp(self):
        """Create a note used by the tests."""
        self.note = StickyNote.objects.create(
            title="First note",
            content="Remember to finish my project.",
        )

    def test_note_list_page_loads(self):
        """The home page should show the notes list."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First note")

    def test_note_detail_page_loads(self):
        """A note detail page should display its content."""
        response = self.client.get(
            reverse("note_detail", kwargs={"pk": self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Remember to finish my project.")

    def test_user_can_create_note(self):
        """A valid form submission should save a new note."""
        response = self.client.post(
            reverse("note_create"),
            {"title": "New note", "content": "Practice Django"},
        )
        self.assertRedirects(response, reverse("note_list"))
        self.assertTrue(StickyNote.objects.filter(title="New note").exists())

    def test_user_can_update_note(self):
        """A valid edit should change the existing note."""
        response = self.client.post(
            reverse("note_update", kwargs={"pk": self.note.pk}),
            {"title": "Updated note", "content": "Updated content"},
        )
        self.assertRedirects(
            response,
            reverse("note_detail", kwargs={"pk": self.note.pk}),
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated note")

    def test_user_can_delete_note(self):
        """A confirmed POST request should delete the note."""
        response = self.client.post(
            reverse("note_delete", kwargs={"pk": self.note.pk})
        )
        self.assertRedirects(response, reverse("note_list"))
        self.assertFalse(StickyNote.objects.filter(pk=self.note.pk).exists())
