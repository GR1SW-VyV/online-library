from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Value, Case, When, BooleanField
from django.shortcuts import render, redirect

from annotations.models import PageNote, PageNoteDAO
from social.models import User
from articles.models import Document


# Create your views here.
@login_required
def book_user_notes(request, document_id):
    current_user = request.user
    document = Document.objects.get(uid=document_id)
    notes = PageNoteDAO.get_all_notes_of_document(current_user.id, document_id)
    page_counter = int(request.GET.get('page', 1))

    # Partial note update/delete
    if request.GET.get('action'):
        note_id = request.GET.get('action').split("_")[1]
        action = request.GET.get('action').split('_')[0]

        if action == 'favorite':
            handle_favorite(note_id)
        elif action == 'delete':
            handle_delete(note_id)

        return redirect(f'/annotations/book/{document_id}/?page={page_counter}')

    # Create a note

    if request.method == 'POST':
        annotation_text = request.POST.get('annotation')
        PageNote.objects.create(
            user_id=current_user.id,
            document_id=document_id,
            is_favorite=False,
            content=annotation_text,
            page=page_counter
        )
        # Redirect, to avoid duplicated notes
        return redirect(f'/annotations/book/{document_id}/?page={page_counter}')

    notes = PageNoteDAO.get_notes_by_page(user_id=current_user.id, document_id=document_id, page=page_counter) \
        .annotate(
        is_favorite_order=Case(
            When(is_favorite=True, then=Value(1)),
            default=Value(0),
            output_field=BooleanField()
        )
    ) \
        .order_by('-is_favorite_order', '-date')

    return render(request, '../templates/annotations/my-notes.html',
                  {'document': document,
                   'user': current_user,
                   'notes': notes,
                   'page': page_counter
                   })


def handle_delete(note_id):
    temp_note = PageNote.objects.get(id=note_id)
    temp_note.delete()


def handle_favorite(note_id):
    temp_note = PageNote.objects.get(id=note_id)
    temp_note.is_favorite = not temp_note.is_favorite
    temp_note.save()
