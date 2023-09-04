from django.db import models
from collections import defaultdict


# Create your models here.
class MockDocuments(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    view_count = models.IntegerField(null=False, default=0)


class MockCollections(models.Model):
    files = models.ManyToManyField('MockDocuments')


class MockUser(models.Model):
    preferences = models.JSONField(default=dict)  # {categoria: numeor}
    collections = models.ManyToManyField('MockCollections')  # colecciones de cada usuario

    def has_collections(self):
        return self.collections.exists()
    
    def recollect_preferences(self):
        # Inicializar un diccionario para realizar un seguimiento de las categorías y su recuento.
        category_count = defaultdict(int)

        # Recorrer todas las colecciones del usuario.
        for collection in self.collections.all():
            # Recorrer los documentos dentro de cada colección.
            for document in collection.files.all():
                # Obtener la categoría del documento.
                category = document.category

                # Actualizar el recuento de la categoría.
                category_count[category] += 1

        # Actualizar las preferencias del usuario según el recuento de categorías.
        for category, count in category_count.items():
            # Si la categoría ya existe en las preferencias, aumenta su valor.
            if category in self.preferences:
                self.preferences[category] += count
            # Si la categoría es nueva, agrégala con un valor de 1.
            else:
                self.preferences[category] = 1

        # Guardar las preferencias actualizadas en la base de datos.
        self.save()

    def get_top_categories(self):
        # Ordenar el diccionario preferences por sus valores en orden descendente.
        sorted_preferences = sorted(self.preferences.items(), key=lambda item: item[1], reverse=True)

        # Tomar las tres primeras claves con los valores más altos, si existen.
        top_categories = [item[0] for item in sorted_preferences[:3]]

        return top_categories

    def get_recomendations(categories):
        # Inicializar un diccionario para almacenar los documentos principales por categoría.
        top_documents_by_category = defaultdict(list)

        # Iterar a través de las categorías proporcionadas.
        for category in categories:
            # Filtrar los documentos por categoría y ordenar por vista en orden descendente.
            top_documents = MockDocuments.objects.filter(category=category).order_by('-view_count')[:4]

            # Agregar los documentos principales al diccionario.
            top_documents_by_category[category] = top_documents

        return dict(top_documents_by_category)


