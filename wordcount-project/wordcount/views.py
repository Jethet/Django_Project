from django.http import HttpResponse
from django.shortcuts import render

# function for the home page, to be used in the url path for the home page when
# the user requests the home page:
def homepage(request):
    # what is sent back to the user: the html for the homepage
    return render(request, 'home.html')

def count(request):
    # this gets the text that is entered by the user:
    fulltext = request.GET['fulltext']
    print(fulltext)
    return render(request, 'count.html')
