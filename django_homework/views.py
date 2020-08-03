from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get("username")
    password = request.POST.get("password")
    # email = request.POST.get("email")
    user_obj = auth.authenticate(username=username, password=password)
    if not user_obj:
        return render(request, 'login.html', {"error_message": "Wrong username or password!"})
    else:
        auth.login(request, user_obj)
        path = request.GET.get("next") or "/index/"
        return HttpResponseRedirect(path)


def index(request):
    usr = auth.get_user(request)
    content = {}
    if usr:
        content = {"username": usr.username}
    return render(request, 'index.html', content)


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    username = request.POST.get("username")
    password = request.POST.get("password")
    if User.objects.filter(username=username):
        # todo: 报错方式待改进
        return render(request, 'register.html', {"error_message": "User already exists!"})
    else:
        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect('/index/')



@login_required
def search(request):
    keyword = request.POST.get("keyword")
    return HttpResponse(keyword)


def logout(request):
    if not auth.get_user(request):
        HttpResponse("You need first login then logout!")
    else:
        auth.logout(request)
        return redirect('/login/')

