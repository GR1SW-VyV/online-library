from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:user_username>', views.profile, name='profile'),
    path('feed', views.feed, name='feed'),
    path('follow_collection/<int:collection_id>', views.follow_collection, name='follow_collection'),
    path('follow_reader/<int:user_id>', views.follow_reader, name='follow_reader'),
]
