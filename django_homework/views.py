from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from articles.models import Article
from django.db.models import Q


def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')
    username = request.POST.get("username")
    password = request.POST.get("password")
    # email = request.POST.get("email")
    user_obj = auth.authenticate(username=username, password=password)
    if not user_obj:
        return render(request, 'account/login.html', {"error_message": "Wrong username or password!"})
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
        return render(request, 'account/register.html')
    username = request.POST.get("username")
    password = request.POST.get("password")
    if User.objects.filter(username=username):
        # todo: 报错方式待改进
        return render(request, 'account/register.html', {"error_message": "User already exists!"})
    else:
        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect('/index/')


@login_required
def search(request):
    keyword = request.GET.get("keyword")

    result = Article.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword))

    return HttpResponse(result)


def detail(request, article_id):
    return render(request, "search/result.html", {"article_id": article_id})


def logout(request):
    if not auth.get_user(request):
        HttpResponse("You need first login then logout!")
    else:
        auth.logout(request)
        return redirect('/login/')
