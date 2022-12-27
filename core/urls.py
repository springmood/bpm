from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.list_view, name="projects"),
    path('project/create', views.project_store, name="project-create"),
    path('project/<str:pk>/', views.project, name="project"),
    path('project/<id>',views.detail_view),
    path('project/update/<id>',views.update_view,name="project-update"),
    path('project/delete/<id>',views.delete_view,name="project-delete"),
]
