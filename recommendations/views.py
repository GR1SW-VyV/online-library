from django.shortcuts import render
import articles.models
import bookcollections.models
from articles import models
from bookcollections import models
from social.models import User
from recommendations.models import RecommendationEngine
from articles.choices.category import Category
from django.contrib.auth.decorators import login_required


@login_required
def view_recommendations(request):
    user = User.objects.get(id=request.user.id)

    recomender = RecommendationEngine(user)
    recommendations = recomender.get_recomendations()
    return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})

#@login_required
def view_form_preferences(request):
    print(request.method)
    return render(request, './recommendation/form_preferences.html',)



