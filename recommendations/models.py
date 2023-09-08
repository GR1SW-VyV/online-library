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
        # Initialize a dictionary to keep track of categories and their count.
        category_count = defaultdict(int)

        # Loop through all the user's collections.
        for collection in bookcollections.models.CollectionDAO.get_all_by_user(self.user.id).all():
            # Loop through the documents within each collection.
            for document in articles.models.Document.objects.filter(collections=collection):
                # Get the category of the document.
                category = document.category

                # Update category count.
                category_count[category] += 1

        # Update user preferences based on category count.
        for category, count in category_count.items():
            # If the category already exists in the preferences, increase its value.
            if category in self.user.preferences:
                self.user.preferences[category] += count
            # If the category is new, add it with a value of 1.
            else:
                self.user.preferences[category] = 1

        # Save the updated preferences in the database.
        self.user.save()

    def recive_preferences(self, *preferences):
        # Initialize a dictionary to keep track of categories and their count.
        preferences_count = defaultdict(int)

        for x in preferences:
            preferences_count[x] += 1

        # update user preferences based on preferences
        for category, count in preferences_count.items():
            # If the category already exists in the preferences, increase its value.
            if category in self.user.preferences:
                self.user.preferences[category] += count
            # If the category is new, add it with a value of 1.
            else:
                self.user.preferences[category] = 1

        # Save the updated preferences in the database.
        self.user.save()

    def get_top_categories(self):
        # Generar categorías por colecciones
        self.recollect_preferences()

        # Ordenar el diccionario preferences por sus valores en orden descendente.
        sorted_preferences = sorted(self.user.preferences.items(), key=lambda item: item[1], reverse=True)

        # Tome las tres primeras claves con los valores más altos, si existen.
        top_categories = [item[0] for item in sorted_preferences[:3]]

        # Rellena con cadenas vacías hasta tener 3 elementos.
        while len(top_categories) < 3:
            top_categories.append("")

        return top_categories

    def get_recomendations(self):
        # Selecciona las categorías más altas
        categories = self.get_top_categories()

        # Inicialice un diccionario para almacenar los documentos principales por categoría.
        top_documents_by_category = defaultdict(list)

        # Iterar a través de las categorías proporcionadas.
        for category in categories:
            # Filtrar los documentos por categoría y ordenar por vista en orden descendente.
            top_documents = articles.models.Document.objects.filter(category=category).order_by('-view_count')[:4]

            # Añade los documentos principales al diccionario.
            top_documents_by_category[category] = top_documents

        return dict(top_documents_by_category)

    def recommendation_total(self):
        # Obtención del total de recomendaciones
        recommendations = self.get_recomendations()
        total = 0
        for x in recommendations.values():
            total += len(x)
        return total



