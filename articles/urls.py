from django.urls import path

from . import views

urlpatterns = [
    path('files/<path:file_path>', views.serve_document),
    path('upload', views.show_upload_document),
]