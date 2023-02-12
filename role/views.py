from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from role.models import Role
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def store(request):
    this_title = request.POST['title']

    Role.objects.create(title=this_title)

    return Response({
        "status": "created successful",
    })


@api_view(['GET'])
def getAll(request):
    context = Role.objects.all()
    return Response({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def detail(request, id):

    context = Role.objects.filter(id=id)
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def update(request, id):
    obj = get_object_or_404(Role, id=id)
    form = RoleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/role/"+id)
    else:
        return JsonResponse({
            "error": "data is not found"
        }, safe=False)


@csrf_exempt
def delete(request, id):
    obj = get_object_or_404(Role, id=id)

    if request.method == "POST":
        obj.delete()

    return JsonResponse({
        "status": "deleted successful",
    })
