from django.shortcuts import render
from .models import TestModel

# Create your views here.
def index(request):
    return render(request, 'helloworld.html')
