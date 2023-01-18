from django.urls import path
from project import views

urlpatterns=[
    path('projects', views.getAll, name="projects"),
    path('project/create', views.store, name="project-create"),
    path('project/<id>', views.detail),
    path('project/update/<id>', views.update, name="project-update"),
    path('project/delete/<id>', views.delete, name="project-delete"),


    # ----------------- project member
    path('project/members', views.project_member_list, name="project-members"),
    path('project/member/create', views.project_member_store,
         name="project-member-craete"),
    path('project/member/<id>', views.project_member_detail),
    path('project/member/delete/<id>', views.project_member_delete,
         name="project-member-delete"),
    path('project/member/update/<id>', views.project_member_update,
         name="project-member-update"),

]