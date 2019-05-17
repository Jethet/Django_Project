from django.shortcuts import render
from .models import Post

# This function handles the traffic that lands on the homepage of the blog:
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# This function handles the logic for the 'about'page of the blog:
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
