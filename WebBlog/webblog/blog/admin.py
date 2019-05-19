from django.contrib import admin

# First import the model that you want to show up on the admin page:
from .models import Post

# Register your models on the admin page:
admin.site.register(Post)
