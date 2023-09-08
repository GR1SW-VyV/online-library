from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_recommedation_engine),
    path('preferences/', views.view_form_preferences),
    path('send_preferences/', views.send_preferences),
]

