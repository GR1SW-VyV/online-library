from django.db import models

# Create your models here.

class Review (models.Model):
    content = models.TextField(max_length=300)
    date = models.DateField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # document = models.ForeignKey(Document, on_delete=models.CASCADE)
