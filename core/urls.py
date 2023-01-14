from django.urls import path
from . import views

urlpatterns = [
    # Project
    path('projects', views.project_list, name="projects"),
    path('project/create', views.project_store, name="project-create"),
    path('project/<id>', views.project_detail),
    path('project/update/<id>', views.project_update, name="project-update"),
    path('project/delete/<id>', views.project_delete, name="project-delete"),
    # task url
    path('tasks', views.task_list, name="tasks"),
    path('task/create', views.task_store, name="task-create"),
    path('task/<id>', views.task_detail),
    path('task/update/<id>', views.task_update, name="task-update"),
    path('task/delete/<id>', views.task_delete, name="task-delete"),
    # user
    path('users', views.user_list, name="users"),
    path('user/create', views.user_store, name="user-craete"),
    path('user/<id>', views.user_detail),
    path('user/delete/<id>', views.user_delete, name="user-delete"),
    path('user/update/<id>', views.user_update, name="user-update"),
    # role
    path('roles', views.role_list, name="roles"),
    path('role/create', views.role_store, name="role-craete"),
    path('role/<id>', views.role_detail),
    path('role/delete/<id>', views.role_delete, name="role-delete"),
    path('role/update/<id>', views.role_update, name="role-update"),
    # project member
    path('project/members', views.project_member_list, name="project-members"),
    path('project/member/create', views.project_member_store, name="project-member-craete"),
    path('project/member/<id>', views.project_member_detail),
    path('project/member/delete/<id>', views.project_member_delete, name="project-member-delete"),
    path('project/member/update/<id>', views.project_member_update, name="project-member-update"),
]
