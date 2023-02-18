from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.models import Project, ProjectMember
from user.models import User
from role.models import Role
from project.forms import Form, ProjectMemberForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from rest_framework import status


@api_view(['POST'])
def store(request):
    this_title = request.data['title']
    this_desc = request.data['desc']
    this_slug = request.data['slug']
    this_img = request.data.get('img', False)
    Project.objects.create(title=this_title, desc=this_desc,
                           img=this_img, slug=this_slug)
    return Response({
        "status": "created successful",
    })


@api_view(['GET'])
def getAll(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many=True)
    return Response({'data':serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail(request, id):

    # projects = Project.objects.filter(id=id)
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, id):
    obj = get_object_or_404(Project, id=id)
    form = Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/"+id)
    else:
        return Response({
            "error": "data is not found"
        })


@api_view(['DELETE'])
def delete(request, id):
    obj = get_object_or_404(Project, id=id)

    if request.method == "DELETE":
        obj.delete()

    return Response({
        "status": "deleted successful",
    }, status=status.HTTP_200_OK)


# ----------------------Project Member Views


@api_view(['POST'])
def project_member_store(request):
    this_project_id = request.data['project_id']
    this_user_id = request.data['user_id']
    this_role_id = request.data['role_id']
    project_instance = Project.objects.get(id=this_project_id)
    user_instance = User.objects.get(id=this_user_id)
    role_instance = Role.objects.get(id=this_role_id)

    ProjectMember.objects.create(
        project=project_instance, user=user_instance, role=role_instance)

    return Response({
        "status": "created successful",
    })


@api_view(['GET'])
def project_member_list(request):
    context = ProjectMember.objects.all()
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)

@csrf_exempt
def project_member_detail(request, id):
    context = ProjectMember.objects.filter(id=id)
    return JsonResponse({
        "data": list(context.values())
    }, safe=False)


@csrf_exempt
def project_member_update(request, id):

    obj = get_object_or_404(ProjectMember, id=id)
    form = ProjectMemberForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/project/member/"+id)
    else:
        return JsonResponse({
            "error": "data is not found"
        }, safe=False)


@csrf_exempt
def project_member_delete(request, id):
    obj = get_object_or_404(ProjectMember, id=id)

    if request.method == "POST":
        obj.delete()

    return JsonResponse({
        "status": "deleted successful",
    })
