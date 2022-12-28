from django.shortcuts import get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Project,Task
from .forms import ProjectForm,TaskForm

@csrf_exempt
def project_store(request):
    this_title=request.POST['title']
    this_desc=request.POST['desc']

    Project.objects.create(title=this_title,desc=this_desc)
    return JsonResponse({
        "status":"ok",
    })


@csrf_exempt
def project_list(request):

    context=Project.objects.all()
    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)



@csrf_exempt
def project_detail(request,id):

    # context=Project.objects.get(id=id)
    context=Project.objects.filter(id=id)
    # dd(context)
    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)



@csrf_exempt
def project_update(request,id):
    obj=get_object_or_404(Project,id=id)
    form=ProjectForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/"+id) 
    else:
        return JsonResponse({
            "error" : "data is not found"
        }, safe=False)



@csrf_exempt
def project_delete(request,id):
    obj=get_object_or_404(Project,id=id)

    if request.method=="POST":
        obj.delete()

    return JsonResponse({
        "status":"deleted successful",
    })


# task api
@csrf_exempt
def task_store(request):
    this_title=request.POST['title']
    this_desc=request.POST['desc']
    this_type=request.POST['type']

    Task.objects.create(title=this_title,desc=this_desc,type=this_type)
    return JsonResponse({
        "status":"created successful",
    })


@csrf_exempt
def task_list(request):

    context=Task.objects.all()
    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)



@csrf_exempt
def task_detail(request,id):

    context=Task.objects.filter(id=id)
    return JsonResponse({
        "data" : list(context.values())
    }, safe=False)



@csrf_exempt
def task_update(request,id):

    obj=get_object_or_404(Task,id=id)
    form=TaskForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/task/"+id) 
    else:
        return JsonResponse({
            "error" : "data is not found"
        }, safe=False)



@csrf_exempt
def task_delete(request,id):
    obj=get_object_or_404(Task,id=id)

    if request.method=="POST":
        obj.delete()

    return JsonResponse({
        "status":"deleted successful",
    })

    

   