from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   #<app>/<model>_<viewtype>.html naming convention
    context_object_name = 'posts'
    ordering = ['-date_posted']    # this ensures newest post comes first: minus sign

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



"""
==> These are FUNCTION-BASED VIEWS for 'home' and 'about'.
    The url patterns are directed to specific views, which are these functions,
    and the views handle the logic for the routes and then render the templates.
    These function-based views have been replaced by CLASS-BASED views during
    the tutorial (tutorial 10).

==> This function handles the traffic that lands on the homepage of the blog:
"""
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# This function handles the logic for the 'about'page of the blog:

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
