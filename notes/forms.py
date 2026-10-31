"""Forms used to create and update sticky notes."""

from django import forms

from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    """Validate the title and content entered by the user."""

    class Meta:
        """Connect the form to StickyNote and choose its editable fields."""

        model = StickyNote
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Sticky note title"}),
            "content": forms.Textarea(
                attrs={"placeholder": "Write your note here...", "rows": 6}
            ),
        }
