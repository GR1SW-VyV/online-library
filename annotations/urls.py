from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/', views.mynotes)
]
