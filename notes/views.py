from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NotesForm

# Create your views here.

def all_notes(request):
    """
    Docstring for view_notes

    :param request: Description
    """
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "page_title": "Notes Board",
    }

    return render(request, "notes/all_notes.html", context)

def view_note(request, pk):
    """
    Docstring for view_notes

    :param request: Description
    :param pk: Description
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/view_note.html", {"note": note})

def write_note(request):
    """
    View to write a new sticky note
    """
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            form.save()
            return redirect("all_notes")
    else:
        form = NotesForm()
    return render(request, "notes/write_note.html", {"form": form})

def edit_note(request, pk):
    """
    View to edit a note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("all_notes")

    else:
        form = NotesForm(instance=note)
    return render(request, "notes/write_note.html", {"form": form})


def delete_note(request, pk):
    """
    View to delete a note
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("all_notes")
