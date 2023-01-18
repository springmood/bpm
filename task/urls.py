from django.urls import path
from task import views

urlpatterns = [
    path('tasks', views.getAll, name="tasks"),
    path('task/create', views.store, name="task-create"),
    path('task/<id>', views.detail),
    path('task/update/<id>', views.update, name="task-update"),
    path('task/delete/<id>', views.delete, name="task-delete"),
    path('upload', views.upload, name="upload"),
]
