from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    """
    Display a list of all sticky notes.
    """
    notes = Note.objects.all().order_by('-created_at')
    context = {'notes': notes}
    return render(request, 'notes/note_list.html', context)

def note_create(request):
    """
    Handle the creation of a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    """
    Handle updating an existing note.
    """
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
        
    return render(
        request, 
        'notes/note_form.html', 
        {'form': form, 'note': note}
    )

def note_delete(request, pk):
    """
    Handle deletion of a note.
    """
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
        
    return render(
        request, 
        'notes/note_confirm_delete.html', 
        {'note': note}
    )