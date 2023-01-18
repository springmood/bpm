from django.urls import path
from project import views

urlpatterns=[
    path('projects', views.getAll, name="projects"),
    path('project/create', views.store, name="project-create"),
    path('project/<id>', views.detail),
    path('project/update/<id>', views.update, name="project-update"),
    path('project/delete/<id>', views.delete, name="project-delete"),
]