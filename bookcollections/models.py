from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


# A collection has many books
# A book can be in many collections

# Many-to-Many relationship


class MockUser(models.Model):
    """
    Mocking model to handle dependencies with User model
    """

class MockArticle(models.Model):
    """
    Mocking model to handle dependencies with Article model
    """
    name = models.TextField(null=True)
    collections = models.ManyToManyField("Collection", related_name="books")

    class Category(models.IntegerChoices):
        UNKNOWN = 0, _("UNKNOWN")


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CollectionDAO:
    """
    This class provides data access methods for retrieving collections
    """

    @classmethod
    def get_all_by_user(cls, user_id):
        """
        Retrieve all collections associated with a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            QuerySet: A queryset containing the collections associated with the user.
        """
        return Collection.objects.filter(user_id=user_id)

    @classmethod
    def to_list(cls, collections):
        return list(collections)

    @classmethod
    def get_first(cls, collections):
        cls.to_list(collections)
        return collections[0]

    @classmethod
    def get_collection(cls, collection_id):
        return Collection.objects.get(id=collection_id)

    @classmethod
    def add_book(
            cls,
            collection_ref: Collection | int,
            book_ref: MockArticle | int
    ):
        collection = (collection_ref if type(collection_ref) == Collection
                      else cls.get_collection(collection_ref))
        book = (book_ref if type(collection_ref) == MockArticle
                else MockArticle.objects.get(id=book_ref))
        book.collections.add(collection)
        book.save()

    @classmethod
    def search_by_name(cls, name):
        """
        Search for collections by name.

        Args:
            name (str): The name to search for.

        Returns:
            QuerySet: A queryset containing the collections with names matching the search.
        """
        return Collection.objects.filter(name__icontains=name)

    @classmethod
    def search_by_name_and_user(cls, name, user_id):
        """
        Search for collections by name and user.

        Args:
            name (str): The name to search for.
            user_id (int): The ID of the user.

        Returns:
            QuerySet: A queryset containing the collections with names
            matching the search and associated with the user.
        """
        return Collection.objects.filter(name__icontains=name, user_id=user_id)

    @classmethod
    def search_by_category(cls, category):
        """
        Search for collections by category.

        Args:
            category: The category to search for.

        Returns:
            QuerySet: A queryset containing the collections with the specified category.
        """
        return Collection.objects.filter(category=category)

    @classmethod
    def search_by_category_and_user(cls, category, user_id):
        """
        Search for collections by category and user.

        Args:
            category: The category to search for.
            user_id: The ID of the user.

        Returns:
            QuerySet: A queryset containing the collections
            with the specified category and associated with the user.
        """
        return Collection.objects.filter(category=category, user_id=user_id)

    @classmethod
    def create(
            cls,
            name,
            description,
            is_public,
            category,
            user_ref: User | int
    ):
        user = User.objects.get(id=user_ref) if type(user_ref) == int else user_ref

        collection = Collection.objects.create(
            name=name,
            description=description,
            is_public=is_public,
            category=category,
            user=user
        )
        collection.save()
        return collection

    @classmethod
    def create_with_book(
            cls,
            name,
            description,
            is_public,
            category,
            user_ref: User | int,
            book_ref: MockArticle | int
    ):
        collection = cls.create(
            name, description, is_public, category, user_ref)

        cls.add_book(collection.id, book_ref)
        return collection

    @classmethod
    def add_book_with_name(cls, coll_name, book_name):
        collection = Collection.objects.filter(name=coll_name).first()
        book = MockArticle.objects.filter(name=book_name).first()
        if book is not None:
            book.collections.add(collection)
            book.save()
        collection.save()
