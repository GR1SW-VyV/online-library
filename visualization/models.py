from django.db import models


# Mocks to test scenarios
class MockUser(models.Model):
    """
    Mocking model to handle dependencies with User model
    """


class MockDocument(models.Model):
    """
    Mocking model to handle dependencies with Document model
    """


class GeneralNote(models.Model):
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(MockUser, on_delete=models.CASCADE)
    document = models.ForeignKey(MockDocument, on_delete=models.CASCADE)


class Note(models.Model):
    content = models.TextField()
    date = models.DateField()
    is_favorite = models.BooleanField(default=False)
    page = models.IntegerField()
    user = models.ForeignKey(MockUser, on_delete=models.CASCADE)
    document = models.ForeignKey(MockDocument, on_delete=models.CASCADE)
