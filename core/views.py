from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Project
from django.core import serializers

# Create your views here.

def projects(request):
    return HttpResponse('here are your projects')


def project(request, pk):
    return HttpResponse('Single Proejct ' + str(pk))

@csrf_exempt
def project_store(request):
    this_title=request.POST['title']
    this_desc=request.POST['desc']

    Project.objects.create(title=this_title,desc=this_desc)
    return JsonResponse({
        "status":"ok"
    })


@csrf_exempt
def list_view(request):
    
    context=Project.objects.all()

    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)
