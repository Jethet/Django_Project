from django.shortcuts import render

posts = [
    {
        'author': 'HH',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 16, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 15, 2019'
    }
]

# This function handles the traffic that lands on the homepage of the blog:
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# This function handles the logic for the 'about'page of the blog:
def about(request):
    return render(request, 'blog/about.html')
