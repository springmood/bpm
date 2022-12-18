from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    return HttpResponse('here are your projects')


def project(request, pk):
    return HttpResponse('Single Proejct ' + str(pk))
