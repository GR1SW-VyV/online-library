from django.urls import path

from . import views

urlpatterns = [
    path('resources/<path:file_path>', views.serve_document),
    path('upload', views.show_upload_document_form),
    path('document/<int:document_id>', views.show_document),
]