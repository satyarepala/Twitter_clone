from django.db import models
from django_accounts.models import CustomUser

class Hashtag(models.Model):
    hashtags = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtags

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use ForeignKey for a single author
    message = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
