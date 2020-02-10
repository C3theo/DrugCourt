#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def sessions(request):
    return HttpResponse("Hello, world. You're at the treatment index.")