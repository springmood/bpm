from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.project_list, name="projects"),
    path('project/create', views.project_store, name="project-create"),
    path('project/<id>',views.project_detail),
    path('project/update/<id>',views.project_update,name="project-update"),
    path('project/delete/<id>',views.project_delete,name="project-delete"),
    # task url
    path('tasks', views.task_list, name="tasks"),
    path('task/create', views.task_store, name="task-create"),
    path('task/<id>',views.task_detail),
    path('task/update/<id>',views.task_update,name="task-update"),
    path('task/delete/<id>',views.task_delete,name="task-delete"),
]
