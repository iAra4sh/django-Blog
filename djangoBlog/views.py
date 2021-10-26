from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('---- Hello welcome to about page -----')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('---> Home Page <---')
    return render(request, 'home.html')
