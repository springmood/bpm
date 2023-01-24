from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from django.http import JsonResponse
from user.forms import Form
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def store(request):
    this_first_name = request.data['first_name']
    this_last_name = request.data['last_name']
    this_email = request.data['email']
    this_password = request.data['password']
    this_username=request.data['username']

    user = User()
    user.first_name = this_first_name
    user.last_name = this_last_name
    user.email = this_email
    user.username=this_username
    user.set_password(this_password)
    user.save()

    return Response({
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

