from django.urls import path
from . import views

urlpatterns = [
    path('recommended/', views.view_recommendations),
    path('preferences/', views.view_form_preferences),
]

