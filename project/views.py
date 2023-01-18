from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.models import Project,ProjectMember
from project.forms import Form,ProjectMemberForm

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



# ----------------------Project Member Views


@csrf_exempt
def project_member_store(request):
    this_project_id = request.POST['project_id']
    this_user_id = request.POST['user_id']
    this_role_id = request.POST['role_id']
    # project_member = ProjectMember()
    # project_member.project_id = this_project_id
    # project_member.user_id = this_user_id
    # project_member.role_id = this_role_id
    # project_member.save()

    ProjectMember.objects.create(
        project_id=this_project_id, user_id=this_user_id, role_id=this_role_id)

    return JsonResponse({
        "status": "created successful",
    })


@csrf_exempt
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
