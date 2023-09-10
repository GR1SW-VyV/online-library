from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from articles.models import Document
from social.models import User
from .models import GeneralNote, GeneralNoteDAO


# Create your views here.
@login_required
def document_info(request, document_id):
    document = Document.objects.get(uid=document_id)
    username = request.user.username
    general_notes = GeneralNoteDAO.get_general_notes(username,document_id)
    context = {
        'document': document,
        'document_notes': general_notes
    }
    return render(request, 'annotations/document_info.html', context)
