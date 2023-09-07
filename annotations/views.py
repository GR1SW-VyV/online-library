from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from annotations.models import Note, NoteDAO
from social.models import User
from articles.models import Document


# Create your views here.
def mynotes(request):
    return render(request, '../templates/annotations/my-notes.html')


# @login_required
def book_user_notes(request, document_id):
    current_user = User.objects.get(id=1)

    document = Document.objects.get(uid=document_id)
    notes = NoteDAO.get_all_notes_of_document(current_user.id, document_id)
    return render(request, '../templates/annotations/my-notes.html', {'document': document, 'user': current_user,
                                                                      'notes': notes})

