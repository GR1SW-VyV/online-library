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
    preferences = models.JSONField(default=dict)  # {category: number}
    collections = models.ManyToManyField('MockCollections')  # collections of each user

    def has_collections(self):
        return self.collections.exists()

    def recollect_preferences(self):
        # Initialize a dictionary to keep track of categories and their count.
        category_count = defaultdict(int)

        # Loop through all the user's collections.
        for collection in self.collections.all():
            # Loop through the documents within each collection.
            for document in collection.files.all():
                # Get the category of the document.
                category = document.category

                # Update category count.
                category_count[category] += 1

        # Update user preferences based on category count.
        for category, count in category_count.items():
            # If the category already exists in the preferences, increase its value.
            if category in self.preferences:
                self.preferences[category] += count
            # If the category is new, add it with a value of 1.
            else:
                self.preferences[category] = 1

        # Save the updated preferences in the database.
        self.save()

    def recive_preferences(self, *preferences):
        # Initialize a dictionary to keep track of categories and their count.
        preferences_count = defaultdict(int)

        for x in preferences:
            self.preferences[x] += 1

        # update user preferences according to preferences
        for category, count in preferences_count.items():
            # If the category already exists in the preferences, increase its value.
            if category in self.preferences:
                self.preferences[category] += count
            # If the category is new, add it with a value of 1.
            else:
                self.preferences[category] = 1

        # Save the updated preferences in the database.
        self.save()

    def get_top_categories(self):
        # Generate categories by collections
        self.recollect_preferences()

        # Sort the preferences dictionary by its values in descending order.
        sorted_preferences = sorted(self.preferences.items(), key=lambda item: item[1], reverse=True)

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
            # Filter documents by category and sort by view in descending order.
            top_documents = MockDocuments.objects.filter(category=category).order_by('-view_count')[:4]

            # Add the main documents to the dictionary.
            top_documents_by_category[category] = top_documents

        return dict(top_documents_by_category)

    def recomendation_by_category(self):
        # get recommendations and categories
        recomendations = self.get_recomendations()
        categories = list(recomendations.keys())

        # Add tuples ("", 0) to fill up to 3 tuples
        while len(categories) < 3:
            categories.append("")

        # Iterate through the categories and emit the tuples
        for category in categories:
            yield category, len(recomendations.get(category, []))


