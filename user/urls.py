from django.urls import path
from user import views
from django.urls import path

urlpatterns=[
    path('users', views.getAll, name="users"),
    path('user/create', views.store, name="user-craete"),
    path('user/<id>', views.detail),
    path('user/delete/<id>', views.delete, name="user-delete"),
    path('user/update/<id>', views.update, name="user-update"),
]