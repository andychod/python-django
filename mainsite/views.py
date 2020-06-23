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
