from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def my_blog_test(request):
    return HttpResponse("Hello, this is the Mind Flora blog!")
