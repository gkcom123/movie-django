from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['A',"B", "Kashmir"]
    }
    return render(request, 'movies/index.html',context)

def about(request):
    return render(request, "movies/about.html", {})
def hello(request,first_name):
    return HttpResponse(f"Hello  page {first_name}")
def add(request,num1,num2):
    return HttpResponse(f"Hello  page {num1+num2}")