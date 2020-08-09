from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from articles.models import Article
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def login(request):
    if request.method == "GET":
        next_step = request.GET.get("next")
        return render(request, 'account/login.html', {"next":next_step})
    username = request.POST.get("username")
    password = request.POST.get("password")
    # email = request.POST.get("email")
    user_obj = auth.authenticate(username=username, password=password)
    if not user_obj:
        return render(request, 'account/login.html', {"error_message": "Wrong username or password!"})
    else:
        auth.login(request, user_obj)
        path = request.POST.get("next") if request.POST.get("next") != "None" and request.POST.get("next") else "/index/"
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
    username = auth.get_user(request).username
    keyword = request.GET.get("keyword")

    time = datetime.datetime.now()
    result = Article.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword))
    timedelta = datetime.datetime.now() - time
    p = Paginator(result.order_by("-time", "title"), 10)
    page = request.GET.get("page")
    content = {
        "used_time": timedelta.total_seconds(),
        "keyword": keyword,
        "username": username,
        "num_pages": p.num_pages,
        "total_results": result.count()
    }
    cur_page = page
    if not page:
        content["result"] = p.page(1)
        content["cur_page"] = 1
        cur_page = 1
    else:
        try:
            content["result"] = p.page(page)
            content["cur_page"] = page
            cur_page = int(page)
        except PageNotAnInteger:
            content["result"] = p.page(1)
            content["cur_page"] = 1
            cur_page = 1
        except EmptyPage:
            content["result"] = p.page(p.num_pages)
            content["cur_page"] = p.num_pages
            cur_page = p.num_pages
    content["page_list"] = range(max(1, cur_page-3), min(p.num_pages, cur_page + 3)+1)
    return render(request, "search/result.html", content)


def detail(request, article_id):
    username = auth.get_user(request).username
    article = get_object_or_404(Article, pk=article_id)
    paras = article.content.split('\n')
    # article.content = content
    return render(request, "search/detail.html", {"article": article, "content": paras, "username": username})


def logout(request):
    if not auth.get_user(request):
        HttpResponse("You need first login then logout!")
    else:
        auth.logout(request)
        return redirect('/login/')

