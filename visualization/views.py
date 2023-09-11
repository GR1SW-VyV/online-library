from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from articles.models import Document
from social.models import User
from .models import GeneralNote, GeneralNoteDAO


# Create your views here.
@login_required
def document_info(request, document_id):
    document = Document.objects.get(uid=document_id)
    user_id = request.user.id
    document.increase_view_count()
    username = request.user.username
    general_notes = GeneralNoteDAO.get_general_notes(username,document_id)
    context = {
        'document': document,
        'document_notes': general_notes
    }

    # Create a general note

    if request.method == 'POST':
        annotation_text = request.POST.get('general_annotation')
        GeneralNote.objects.create(
            user_id=user_id,
            document_id=document_id,
            content=annotation_text
        )
        # Redirect, to avoid duplicated notes
        return redirect(f'/visualization/document/{document_id}')

    return render(request, 'annotations/document_info.html', context)
