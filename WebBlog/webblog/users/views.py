from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # An existing Django form

# Create your views here.

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
