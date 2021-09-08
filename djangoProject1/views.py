from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, '../FA/template/homepage.html')


def about(request):
    return render(request, '../FA/template/about.html')
