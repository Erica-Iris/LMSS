from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    html = '<p>aaa</p>'
    return HttpResponse(html)
