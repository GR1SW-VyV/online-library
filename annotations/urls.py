from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/', views.mynotes),
    path('book/<int:document_id>/', views.book_user_notes, name='book_user_notes'),
]

