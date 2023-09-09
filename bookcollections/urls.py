from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_collections),
    path('create/', views.create_coll),
    path('<int:id>', views.view_singe_collection)
]