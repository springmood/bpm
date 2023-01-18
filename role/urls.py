from django.urls import path
from role import views

urlpatterns = [
    path('roles', views.getAll, name="roles"),
    path('role/create', views.store, name="role-craete"),
    path('role/<id>', views.detail),
    path('role/delete/<id>', views.delete, name="role-delete"),
    path('role/update/<id>', views.update, name="role-update"),
]
