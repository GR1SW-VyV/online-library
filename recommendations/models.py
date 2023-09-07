from django.db import models
from collections import defaultdict

import articles.models
import bookcollections.models
from articles import models
from bookcollections import models
from social.models import User
# Create your models here.



class RecommendationEngine:

    def __init__(self, user):
        self.user = user

    def has_collections(self):
        return bookcollections.models.Collection.objects.filter(user=self.user).exists()

    def recollect_preferences(self):
        # Inicialice un diccionario para realizar un seguimiento de las categorías y su recuento.
        category_count = defaultdict(int)

        # Recorrer todas las colecciones del usuario.
        for collection in bookcollections.models.CollectionDAO.get_all_by_user(self.user.id).all():
            # Recorrer los documentos dentro de cada colección.
            for document in articles.models.Document.objects.filter(collections=collection):
                # Obtener la categoría del documento.
                category = document.category

                # Actualizar el recuento de categorías.
                category_count[category] += 1

        # Actualice las preferencias del usuario según el recuento de categorías.
        for category, count in category_count.items():
            # Si la categoría ya existe en las preferencias, aumenta su valor.
            if category in self.user.preferences:
                self.user.preferences[category] += count
            # Si la categoría es nueva, agrégala con un valor de 1.
            else:
                self.user.preferences[category] = 1

        # Guardar las preferencias actualizadas en la base de datos.
        self.user.save()

    def recive_preferences(self, *preferences):
        # Initialize a dictionary to keep track of categories and their count.
        preferences_count = defaultdict(int)

        for x in preferences:
            preferences_count[x] += 1

        # update user preferences according to preferences
        for category, count in preferences_count.items():
            # Si la categoría ya existe en las preferencias, aumenta su valor.
            if category in self.user.preferences:
                self.user.preferences[category] += count
            # Si la categoría es nueva, agrégala con un valor de 1.
            else:
                self.user.preferences[category] = 1

        # Guardar las preferencias actualizadas en la base de datos.
        self.user.save()

    def get_top_categories(self):
        # Generate categories by collections
        self.recollect_preferences()

        # Ordenar el diccionario preferences por sus valores en orden descendente.
        sorted_preferences = sorted(self.user.preferences.items(), key=lambda item: item[1], reverse=True)

        # Take the first three keys with the highest values, if they exist.
        top_categories = [item[0] for item in sorted_preferences[:3]]

        # Fill with empty strings until you have 3 elements
        while len(top_categories) < 3:
            top_categories.append("")

        return top_categories

    def get_recomendations(self):
        # Select the highest categories
        categories = self.get_top_categories()

        # Initialize a dictionary to store the main documents by category.
        top_documents_by_category = defaultdict(list)

        # Iterate through the provided categories.
        for category in categories:
            # Filtrar los documentos por categoría y ordenar por vista en orden descendente.
            top_documents = articles.models.Document.objects.filter(category=category).order_by('-view_count')[:4]

            # Add the main documents to the dictionary.
            top_documents_by_category[category] = top_documents

        return dict(top_documents_by_category)

    def recommendation_total(self):
        recommendations = self.get_recomendations()
        total = 0
        for x in recommendations.values():
            total += len(x)
        return total



