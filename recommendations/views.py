from django.shortcuts import render, redirect

from social.models import User
from recommendations.models import RecommendationEngine
from django.contrib.auth.decorators import login_required

categories_dict = {'MATH': 'Matemática', 'PHYSICS': 'Física', 'CALCULUS': 'Cálculo',
                   'PROGRAMMING': 'Programación', 'LITERATURE': 'Literatura',
                   'GEOMETRY': 'Geometría', 'ECONOMY': 'Economía', 'CHEMISTRY': 'Química'}


@login_required
def init_recommedation_engine(request):
    user = request.user
    recomender = RecommendationEngine(user)
    if recomender.has_collections():
        recommendations = recomender.get_recomendations()
        for recommendation in recommendations:
            category = recommendation['category']
            if category in categories_dict:
                recommendation['category'] = categories_dict[category]
                # Check if recommended list has some recommendations
                if recommendation['books']:
                    return render(request, './recommendation/recommended.html',
                                  context={'recommendations': recommendations})
                # It happens went user has collections without any book
                else:
                    mensaje = 'Al parecer no tienes libros asignados a tus colecciones'
                    return render(request, './recommendation/form_preferences.html', context={'mensaje': mensaje})
    else:
        mensaje = 'No tienes colecciones creadas aún'
        return render(request, './recommendation/form_preferences.html', context={'mensaje': mensaje})


@login_required
def view_form_preferences(request):
    print(request.method)
    return render(request, './recommendation/form_preferences.html', )


@login_required
def send_preferences(request):
    user = User.objects.get(id=request.user.id)
    recomender = RecommendationEngine(user)
    if request.method == 'POST':
        # Acces categories wich are selected
        selected_categories = request.POST.getlist('categorias[]')
        if len(selected_categories) == 0:
            mensaje = 'Debe seleccionar al menos 1 categoría'
            return redirect('/recommendations', context={'mensaje': mensaje})
        else:
            tuple_selected_categories = tuple(selected_categories)
            # Call specific view
            recomender.recive_preferences(*tuple_selected_categories)
            recommendations = recomender.get_recomendations()
            for recommendation in recommendations:
                category = recommendation['category']
                if category in categories_dict:
                    recommendation['category'] = categories_dict[category]
            return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})


