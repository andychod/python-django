from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from mainsite import models


# 唐詩網頁用
def tang_poetry(request):
    posts = models.Post.objects.all()
    now = datetime.now()
    return render(request, 'tang_poetry/tang_poetry_index.html', locals())

def tang_poetry_showpost(request, slug):
    print(slug)
    try:
        post = models.Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'tang_poetry/tang_poetry_post.html', locals())
    except:
        return redirect('/')

# 直播網頁用
def live_index(request, tvno = 0):
    tv_list = [
        {'name':'東森', 'tvcode':'RaIJ767Bj_M'},
        {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
        {'name': '台視', 'tvcode': 'yk2CUjbyyQY'},
        {'name': '華視', 'tvcode': 'TL8mmew3jb8'},
        {'name': '三立', 'tvcode': '4ZVUmEUFwaY'},
        {'name': '中天', 'tvcode': 'hgIfZz8STLk'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    hour = now.timetuple().tm_hour
    return render(request, 'livenews/index.html', locals())

def live_entv(request, tvno = 0):
    tv_list = [
        {'name': 'SkyNews', 'tvcode':'9Auq9mYxFEE'},
        {'name': 'Euro News', 'tvcode': '6xrJy-1_qS4'},
        {'name': 'India News', 'tvcode': 'l9ViEIip9q4'},
        {'name': 'CNA', 'tvcode': 'U_XsRZXL2Ic'}
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    hour = now.timetuple().tm_hour
    return render(request, 'livenews/entv.html', locals())
