from django.db import models
# from django.contrib.auth.models import User
from social.models import Observable, CollectionActivity, User
from django.utils.translation import gettext_lazy as _
from articles.choices.category import Category


# A collection has many books
# A book can be in many collections

# Many-to-Many relationship


class Collection(models.Model, Observable):
    """
    Model representing a collection of books.
    """
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_public = models.BooleanField(default=False, null=False)
    category = models.CharField(
        max_length=100,
        choices=Category.choices,
        default=Category.UNKNOWN
    )
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, symmetrical=False, blank=True, related_name='collection_following')

    def add_follower(self, observer):
        self.followers.add(observer)

    def create_collection_activity(self, document):
        activity = CollectionActivity()
        activity.collection = self
        activity.document = document
        activity.detail = "add a new document"
        activity.save()
        self.add_activity(activity)

    def notify(self):
        for follower in self.followers.all():
            follower.update(self.activities[-1])


from articles.models import Document


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
            cls, collection_ref: Collection | int, book_ref: Document | int
    ):
        collection = (
            collection_ref
            if type(collection_ref) == Collection
            else cls.get_collection(collection_ref)
        )
        '''
        book = (
            book_ref
            #if type(collection_ref) == Document
            #else Document.objects.get(uid=book_ref)
        )
        '''
        book = book_ref
        if type(book) == int:
            book = Document.objects.get(uid=book)
        book.collections.add(collection)
        #TODO collection.score = cls.get_collection_score(collection.id) Hagan bien
        collection.save()
        book.save()
        collection.create_collection_activity(book)

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
    def create(cls, name, description, is_public, category, user_ref: User | int):
        user = User.objects.get(id=user_ref) if type(user_ref) == int else user_ref

        collection = Collection.objects.create(
            name=name,
            description=description,
            is_public=is_public,
            category=category,
            user=user,
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
            book_ref: Document | int,
    ):
        collection = cls.create(name, description, is_public, category, user_ref)

        cls.add_book(collection.id, book_ref)
        return collection

    @classmethod
    def add_book_with_name(cls, coll_name, book_name):
        collection = Collection.objects.filter(name=coll_name).first()
        book = Document.objects.filter(title=book_name).first()
        if book is not None:
            book.collections.add(collection)
            book.save()
            collection.score = cls.calculate_collection_score(collection.id)
        collection.save()

    @classmethod
    def calculate_collection_score(cls, collection_ref: int | str):
        if type(collection_ref) == str:
            collection = Collection.objects.filter(name=collection_ref).first()
        else:
            collection = Collection.objects.get(id=collection_ref)
        books = collection.books.all()
        score = 0
        for book in books:
            score += book.score()
        return score / len(books)
