from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def Index(request: HttpRequest):
    return render(request, 'Admin_Panel/Dashboard/Index.html', {})


def All_Articles(request: HttpRequest):
    return render(request, 'Admin_Panel/Articles/Articles_List.html', {})