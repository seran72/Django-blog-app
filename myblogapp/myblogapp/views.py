#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
#    return HttpResponse('Hello World. Home Page')
    return render(request, 'home.html')

# When routing to /about url, it will request this function
def about(request):
#    return HttpResponse('My about page')
    return render(request, 'about.html')

