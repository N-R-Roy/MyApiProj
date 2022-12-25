from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("student-list/", views.student_list, name='student_list'),
    path("login/", views.login, name="login"),
    path("login_handler/", views.login_handler, name="login_handler"),
]
