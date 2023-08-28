from django.db import models
from django.utils.translation import gettext_lazy as _


# A collection has many books
# A book can be in many collections

# Many to Many relationship

class MockArticle(models.Model):
    """
    Mocking model to handle dependencies with Article model
    """
    class Category(models.IntegerChoices):
        UNKNOWN = 0, _('UNKNOWN')

    collections = models.ManyToManyField('Collection', related_name='books')


class Collection(models.Model):
    """
    Model representing a collection of books.
    """
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_public = models.BooleanField(default=False, null=False)

    category = models.CharField(
        max_length=100,
        choices=MockArticle.Category.choices,
        default=MockArticle.Category.UNKNOWN
    )

    def __str__(self):
        return self.name

    def get_collection(self, collection_id):
        pass

    def add_book(self, book):
        pass

    def create(self, collection):
        pass

# get all collections by user
# get collection by id

# Search by name, category
# 2 fncs:
    # results in general
    # results by user


class CollectionDAO():
    @classmethod
    def get_all_by_user(cls, user_id):
        return Collection.objects.filter(user_id=user_id)

    @classmethod
    def get_collection(cls, collection_id):
        return Collection.objects.get(id=collection_id)

    @classmethod
    def add_book(cls, collection_id, book_id):
        collection = cls.get_collection(collection_id)
        book = MockArticle.objects.get(id=book_id)
        book.collections.add(collection)
        book.save()

    @classmethod
    def search_by_name(cls, name):
        return Collection.objects.filter(name__icontains=name)

    @classmethod
    def search_by_name_and_user(cls, name, user_id):
        return Collection.objects.filter(name__icontains=name, user_id=user_id)

    @classmethod
    def search_by_category(cls, category):
        return Collection.objects.filter(category=category)

    @classmethod
    def search_by_category_and_user(cls, category, user_id):
        return Collection.objects.filter(category=category, user_id=user_id)
