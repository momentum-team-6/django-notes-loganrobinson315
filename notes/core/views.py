from django.shortcuts import render, redirect, get_object_or_404
from core.data import NOTES
from core.models import Note
from .forms import NoteForm

# Create your views here.
def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'core/index.html', {'notes': notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "core/note_detail.html", {'note': note})


def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')

    return render(request, "core/add_note.html", {'form': form})