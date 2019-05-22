from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post



"""
==> These are FUNCTION-BASED VIEWS for 'home' and 'about'.
    The url patterns are directed to specific views, which are these functions,
    and the views handle the logic for the routes and then render the templates.
    These function-based views have been replaced by CLASS-BASED views during
    the tutorial (tutorial 10).

==> This function handles the traffic that lands on the homepage of the blog:

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

==> This function handles the logic for the 'about'page of the blog:

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
"""
