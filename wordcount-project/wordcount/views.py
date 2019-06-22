from django.http import HttpResponse

# function for the home page, to be used in the url path for the home page when
# the user requests the home page:
def home(request):
    # what is sent back to the user:
    return HttpResponse('Hello')
