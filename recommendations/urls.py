from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommendations, name='hello'),
    path('profile/<int:user_id>', views.form_preferences, name='profile'),
]

