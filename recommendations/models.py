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
        # check if collections exist
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
        # Generate categories by collections
        self.recollect_preferences()

        # Sort the preferences dictionary by its values in descending order.
        sorted_preferences = sorted(self.user.preferences.items(), key=lambda item: item[1], reverse=True)

        # Take the first three keys with the highest values, if they exist.
        top_categories = [item[0] for item in sorted_preferences[:3]]

        # Fill with empty strings until you have 3 elements.
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
            top_documents = articles.models.Document.objects.filter(category=category).order_by('-view_count')[:4]

            # Add the main documents to the dictionary.
            top_documents_by_category[category] = top_documents

        return dict(top_documents_by_category)

    def recommendation_total(self):
        # Getting Recommendations
        recommendations = self.get_recomendations()
        total = 0
        # iterate to calculate total recommendations
        for x in recommendations.values():
            total += len(x)
        return total



