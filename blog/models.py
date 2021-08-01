from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    Let’s keep things simple and assume each post has a title,
    author and body. This class turn this into a database model
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
