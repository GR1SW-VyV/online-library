from django.urls import path
from . import views

urlpatters = [
    path('document/<int:document_id>',views.document_info)
]