from django.db import models


# Create your models here.
class Note(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #document = models.ForeignKey(Document, on_delete=models.CASCADE)
