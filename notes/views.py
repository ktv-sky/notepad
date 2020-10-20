from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Note
from .forms import NoteModelForm


@login_required
def note_list_view(request):
    form = NoteModelForm()
    if request.method == 'POST':
        form = NoteModelForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.save()
            return redirect('note-list')
    to_do_list = Note.objects.filter(finished=False, owner=request.user)
    finished_list = Note.objects.filter(finished=True, owner=request.user)

    return render(request, 'notes/note_list.html', {
        'to_do_list': to_do_list,
        'finished_list': finished_list,
        'form': form,
    })


@login_required
def finish_item(request, id):
    note = get_object_or_404(Note, id=id)
    check_note_owner(note.owner, request.user)
    note.finished = True
    note.save()

    return redirect('note-list')


@login_required
def delete_item(request, id):
    note = get_object_or_404(Note, id=id)
    check_note_owner(note.owner, request.user)
    note.delete()

    return redirect('note-list')


@login_required
def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    check_note_owner(note.owner, request.user)
    note.finished = False
    note.save()

    return redirect('note-list')


def check_note_owner(owner, user):
    if owner != user:
        raise Http404
