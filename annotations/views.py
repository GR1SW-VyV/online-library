from django.shortcuts import render, get_object_or_404
from annotations.models import Note, NoteDAO


# Create your views here.
def mynotes(request):
    return render(request, '../templates/annotations/my-notes.html')


def book_user_notes(request, document_id):
    user_id = request.POST.get('user_id')
    notes = NoteDAO.get_all_notes_of_document(user_id, document_id)

    return render(request, '../templates/annotations/my-notes.html', {'notes': notes, 'book_id': document_id})
