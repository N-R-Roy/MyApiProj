from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo
from .forms import LoginForm, AForm


def index(request):
    request.session['value'] = "index add"
    request.session["page"] = ["index"]
    return render(request, 'myapp/index.html')


def student_list(request):
    status = ""
    value = request.session['value']
    if request.session.get("page"):
        for pg in request.session.get("page"):
            status = status + pg + ", "
        # plist = request.session.get("page")
        # plist.append("s_list")
        if 's_list' not in request.session.get("page"):
            request.session.get("page").append("s_list")
        request.session['value'] = 's_list add'
        # print(plist)
        print(dict(request.session))
        # request.session['page'] = plist
    else:
        status = 'Empty'
        request.session['page'] = ['s_list']

    students = StudentInfo.objects.all()

    data = {"students": students, 'status': status, 'value': value}

    return render(request, 'myapp/show_student.html', data)


def login(request):
    login_form = LoginForm()
    aform = AForm()
    return render(request, "myapp/login.html", {'login_form': login_form, "aform": aform})


def login_handler(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data["name"]
            address = login_form.cleaned_data["address"]
            mob_no = login_form.cleaned_data["mob_no"]

            result = name + " >> " + address + " >> " + mob_no

            return HttpResponse(result)

