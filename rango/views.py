from django.shortcuts import rendera
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says HHHHHHHELLO WORLD!")
