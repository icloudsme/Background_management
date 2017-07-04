#coding:utf8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("大功告成，搞定第一个页面")
    return render(request, "blog2/index.html", {"hello": "2"})