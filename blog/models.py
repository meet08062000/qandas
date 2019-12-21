# Create your models here.
# from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    liked_or_not = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Answers(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    
    def __str__(self):
        return self.text
