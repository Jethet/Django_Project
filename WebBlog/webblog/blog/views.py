from django.shortcuts import render
from django.http import HttpResponse

# This function handles the traffic that lands on the homepage of the blog:
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
