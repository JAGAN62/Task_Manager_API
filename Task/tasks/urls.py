from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),

    path("tasks/", views.task_list, name="task_list"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/detail/<int:pk>/", views.task_detail, name="task_detail"),
    path("tasks/update/<int:pk>/", views.update_task, name="update_task"),
    path("tasks/delete/<int:pk>/", views.delete_task, name="delete_task"),
]