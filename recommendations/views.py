from django.shortcuts import render

import social.models
from social.models import User
from recommendations.models import RecommendationEngine
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from bookcollections import models
from articles.choices.category import Category
from django.http import HttpResponse


def init_recommedation_engine(request):
    # Test
    user = User.objects.create_reader_user(username="test28", password="123")

    # collection_1 = models.CollectionDAO.create(
    #    "Coleccion 1",
    #    "Descripcion",
    #    True,
    #    Category.GEOMETRY,
    #    user
    # )

    # user = authenticate(request, username="test8", password="123")

    # user = User.objects.get(id=request.user.id)
    if user is not None:
        login(request, user)
    recomender = RecommendationEngine(user)
    if recomender.has_collections():
        recommendations = recomender.get_recomendations()
        return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})
    else:
        return render(request, './recommendation/form_preferences.html', )


@login_required
def view_form_preferences(request):
    print(request.method)
    return render(request, './recommendation/form_preferences.html', )


def send_preferences(request):
    user = User.objects.get(id=request.user.id)
    recomender = RecommendationEngine(user)
    if request.method == 'POST':
        # Acces categories wich are selected
        selected_categories = request.POST.getlist('categorias[]')
        tuple_selected_categories = tuple(selected_categories)
        # Test
        print(tuple_selected_categories)
        # Call specific view
        recomender.recive_preferences(*tuple_selected_categories)
        recommendations = recomender.get_recomendations()
        return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})
