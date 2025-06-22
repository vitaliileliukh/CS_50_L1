from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def vitalii(request):
    return HttpResponse("Hello, Vitalii!")

def sasha(request):
    return HttpResponse("Hello, Sasha!")

def greet(request, name): #
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })