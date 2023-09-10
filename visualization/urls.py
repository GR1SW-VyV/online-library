from django.urls import path
from . import views

urlpatterns = [
    path('document/<int:document_id>',views.document_info)
]