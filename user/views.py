from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from django.http import JsonResponse
from user.forms import Form

@csrf_exempt
def store(request):
    this_fname = request.POST['fname']
    this_lname = request.POST['lname']
    this_email = request.POST['email']
    this_password = request.POST['password']
    this_username=request.POST['username']

    # User.objects.create(fname=this_fname,lname=this_lname,email=this_email,password=this_password)
    user = User()
    user.fname = this_fname
    user.lname = this_lname
    user.email = this_email
    user.username=this_username
    user.set_password(this_password)
    user.save()

    return JsonResponse({
        "status": "created successful",
    })


@csrf_exempt
def getAll(request):
    context = User.objects.all()
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def detail(request, id):

    context = User.objects.filter(id=id)
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def update(request, id):

    obj = get_object_or_404(User, id=id)
    form = Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.password = obj.set_password(request.POST['password'])
        form.save()
        return redirect("/user/"+id)
    else:
        return JsonResponse({
            "error": "data is not found"
        }, safe=False)


@csrf_exempt
def delete(request, id):
    obj = get_object_or_404(User, id=id)

    if request.method == "POST":
        obj.delete()

    return JsonResponse({
        "status": "deleted successful",
    })

