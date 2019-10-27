from django.db import models
from django.utils import timezone
from django.urls import reverse

# Importing Django user model
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Made so as to redirect to the post after it;s creation(using the django built in class views)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})