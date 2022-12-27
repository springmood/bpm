from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Project
from .forms import ProjectForm
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
        "status":"ok",
    })


@csrf_exempt
def list_view(request):
    
    context=Project.objects.all()

    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)

@csrf_exempt
def detail_view(request,id):

    # context=Project.objects.get(id=id)
    context=Project.objects.filter(id=id)
    # dd(context)
    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)

@csrf_exempt
def update_view(request,id):
    obj=get_object_or_404(Project,id=id)
    form=ProjectForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/"+id) 
    else:
        return JsonResponse({
            "error" : "data is not fount"
        }, safe=False)

@csrf_exempt
def delete_view(request,id):
    obj=get_object_or_404(Project,id=id)

    if request.method=="POST":
        obj.delete()

    return JsonResponse({
        "status":"deleted successful",
    })



    

   