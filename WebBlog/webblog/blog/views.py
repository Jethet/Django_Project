from django.shortcuts import render

# This function handles the traffic that lands on the homepage of the blog:
def home(request):
    return render(request, 'blog/home.html')

# This function handles the logic for the 'about'page of the blog:
def about(request):
    return render(request, 'blog/about.html')
