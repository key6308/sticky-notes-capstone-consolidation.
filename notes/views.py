"""Page views for listing and managing sticky notes."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import StickyNoteForm
from .models import StickyNote


def note_list(request):
    """Show all notes, with the newest note at the top."""
    notes = StickyNote.objects.all().order_by("-id")
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Show one note. Return a 404 page if the note does not exist."""
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Validate and save a new note submitted by the user."""
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = StickyNoteForm()
    return render(
        request,
        "notes/note_form.html",
        {"form": form, "page_title": "Add Sticky Note"},
    )


def note_update(request, pk):
    """Update an existing note after validating the submitted form."""
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = StickyNoteForm(instance=note)
    return render(
        request,
        "notes/note_form.html",
        {"form": form, "page_title": "Edit Sticky Note"},
    )


def note_delete(request, pk):
    """Delete a note only after the user confirms with a POST request."""
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
