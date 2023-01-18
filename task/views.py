from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from task.models import Task
from task.forms import Form, UploadFileForm


@csrf_exempt
def store(request):
    this_title = request.POST['title']
    this_desc = request.POST['desc']
    this_type = request.POST['type']

    Task.objects.create(title=this_title, desc=this_desc, type=this_type)
    return JsonResponse({
        "status": "created successful",
    })


@csrf_exempt
def getAll(request):
    context = Task.objects.all()
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def detail(request, id):

    context = Task.objects.filter(id=id)
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def update(request, id):

    obj = get_object_or_404(Task, id=id)
    form = Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/task/"+id)
    else:
        return JsonResponse({
            "error": "data is not found"
        }, safe=False)


@csrf_exempt
def delete(request, id):
    obj = get_object_or_404(Task, id=id)

    if request.method == "POST":
        obj.delete()

    return JsonResponse({
        "status": "deleted successful",
    })


# upload
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.get('file',False)
        return JsonResponse({"url":str(file)}, safe=False)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
