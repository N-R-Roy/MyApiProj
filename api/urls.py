from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_student, name='get_student'),
    path('student-detail/<str:pk>/', views.student_detail, name='student_detail'),
    path('create-student/', views.create_student, name='create_student'),
    path('update-student/<str:pk>/', views.update_student, name='update_student'),
    path('employees/', views.get_employee, name="get_employee"),
    path('users/', views.get_user, name="get_user"),
]


