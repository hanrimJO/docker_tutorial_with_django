from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('jenkins auto build 5 test')