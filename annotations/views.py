from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from annotations.models import Note, NoteDAO
from social.models import User
from articles.models import Document


# Create your views here.
def mynotes(request):
    return render(request, '../templates/annotations/my-notes.html')


# @login_required
def book_user_notes(request, document_id):
    # user_profile = User.objects.get(id=request.user.id)
    document = Document.objects.get(uid=document_id)
    # notes = NoteDAO.get_all_notes_of_document(user_profile.id, document_id)
    return render(request, '../templates/annotations/my-notes.html', {'document': document})
