from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import StudentInfo, EmployeeInfo, UserInfo
from .serializer import StudentSerializer, EmployeeSerializer, UserSerializer


@api_view(['GET'])
def get_student(request):
    student_list = StudentInfo.objects.all()
    slzr = StudentSerializer(student_list, many=True)
    return Response(slzr.data)


@api_view(['GET'])
def student_detail(request, pk):
    sl = StudentInfo.objects.get(sid=pk)
    slzr = StudentSerializer(sl, many=False)
    return Response(slzr.data)


@api_view(['POST'])
def create_student(request):

    # print(request.data)

    slzr = StudentSerializer(data=request.data)

    if slzr.is_valid():
        slzr.save()

    return Response(slzr.data)


@api_view(['POST'])
def update_student(request, pk):

    s1 = StudentInfo.objects.get(sid=pk)

    slzr = StudentSerializer(instance=s1, data=request.data)

    if slzr.is_valid():
        slzr.save()

    return Response(slzr.data)


@api_view(['GET'])
def get_employee(request):
    employee_list = EmployeeInfo.objects.all()
    emp_slzr = EmployeeSerializer(employee_list, many=True)
    return Response(emp_slzr.data)


@api_view(['GET'])
def get_user(request):
    user_list = UserInfo.objects.all()
    user_slzr = UserSerializer(user_list, many=True)
    return Response(user_slzr.data)

