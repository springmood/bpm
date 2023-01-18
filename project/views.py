from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.models import Project
from project.forms import Form

@csrf_exempt
def store(request):
    this_title = request.POST['title']
    this_desc = request.POST['desc']
    this_img = request.POST.get('img',False)

    Project.objects.create(title=this_title, desc=this_desc,img=this_img)
    return JsonResponse({
        "status": "created successful",
    })


@csrf_exempt
def getAll(request):
    context = Project.objects.all()
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def detail(request, id):

    # context=Project.objects.get(id=id)
    context = Project.objects.filter(id=id)
    # dd(context)
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def update(request, id):
    obj = get_object_or_404(Project, id=id)
    form =Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/"+id)
    else:
        return JsonResponse({
            "error": "data is not found"
        }, safe=False)


@csrf_exempt
def delete(request, id):
    obj = get_object_or_404(Project, id=id)

    if request.method == "POST":
        obj.delete()

    return JsonResponse({
        "status": "deleted successful",
    })

