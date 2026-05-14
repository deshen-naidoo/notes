"""
Views for the Sticky Notes application.
Handles the CRUD operations (Create, Read, Update, Delete).
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def note_list(request):
    """
    Retrieves all notes from the database and renders the list.
    """
    all_notes = Note.objects.all()
    context_data = {"notes": all_notes}
    return render(request, "notes/note_list.html", context_data)

def note_detail(request, pk):
    """
    Retrieves a specific note by its primary key (pk) and renders it.
    Demonstrates robustness using get_object_or_404.
    """
    selected_note = get_object_or_404(Note, pk=pk)
    context_data = {"note": selected_note}
    return render(request, "notes/note_detail.html", context_data)

def note_create(request):
    """
    Handles the creation of a new sticky note using NoteForm.
    """
    if request.method == "POST":
        form_data = NoteForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("note_list")
    else:
        form_data = NoteForm()
        
    context_data = {"form": form_data}
    return render(request, "notes/note_form.html", context_data)

def note_update(request, pk):
    """
    Handles updating an existing sticky note.
    """
    selected_note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        form_data = NoteForm(request.POST, instance=selected_note)
        if form_data.is_valid():
            form_data.save()
            return redirect("note_list")
    else:
        form_data = NoteForm(instance=selected_note)
        
    context_data = {"form": form_data}
    return render(request, "notes/note_form.html", context_data)

def note_delete(request, pk):
    """
    Deletes a specific note and redirects to the list view.
    """
    selected_note = get_object_or_404(Note, pk=pk)
    selected_note.delete()
    return redirect("note_list")