from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from annotations.models import Note, NoteDAO
from social.models import User
from articles.models import Document


# Create your views here.
# @login_required
def book_user_notes(request, document_id):
    current_user = User.objects.get(id=1)

    document = Document.objects.get(uid=document_id)
    page_counter = int(request.GET.get('page', 1))

    # Create a note

    if request.method == 'POST':
        annotation_text = request.POST.get('annotation')
        Note.objects.create(
            user_id=current_user.id,
            document_id=document_id,
            is_favorite=True,
            content=annotation_text,
            page=page_counter
        )
        # Redirect, to avoid duplicated notes
        return redirect(f'/annotations/book/{document_id}/?page={page_counter}')

    notes = NoteDAO.get_notes_by_page(user_id=1, document_id=document_id, page=page_counter).order_by('-date')

    return render(request, '../templates/annotations/my-notes.html',
                  {'document': document,
                   'user': current_user,
                   'notes': notes,
                   'page': page_counter
                   })
