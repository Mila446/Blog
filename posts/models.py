from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
# models is a module that has a bunch of classes w/in it
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default = now,
                                        blank = True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.author} to {self.post}'