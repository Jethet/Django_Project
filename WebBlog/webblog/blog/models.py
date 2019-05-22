from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # this is a one-to-many relationship
from django.urls import reverse

# Django includes various models. These can be used and also adjusted.

# This class inherits from the Django model class. Each class is a table in
# the database. Each attribute is a different field in the database.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, posts are deleted as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
