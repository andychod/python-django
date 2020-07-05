from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from mainsite import models, forms


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

# 心情網頁用
def blog_index(request, pid=None, del_pass=None):
    posts = models.MoodPost.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要張貼信息，則每一個欄位都要填寫'
    if del_pass and pid:
        print("!!!!!")
        print(pid)
        try:
            post = models.MoodPost.objects.get(id=pid)
        except:
            post = None
        print(post)
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = '資料刪除成功'
            else:
                message = '密碼錯誤'
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.MoodPost.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存，請記得你的編輯密碼[{}]! 訊息需經審查後才會顯示。'.format(user_pass)
    return render(request, 'blog/index.html', locals())

def blog_listing(request):
    posts = models.MoodPost.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'blog/listing.html', locals())

def blog_posting(request):
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
    except:
        user_id = None
        message = '如要張貼信息，則每一個欄位都要填寫'
    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.MoodPost.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存，請記得你的編輯密碼[{}]! 訊息需經審查後才會顯示。'.format(user_pass)
    return render(request, 'blog/posting.html', locals())

def blog_contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else:
            message = "請檢察您輸入的資訊是否正確!"
    else:
        form = forms.ContactForm()
    return render(request, 'blog/contact.html', locals())

def blog_post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的訊息已儲存，要等管理者啟用後才看得到"
            post_form.save()
            return HttpResponseRedirect('/blog/list/')
        else:
            message = "如要張貼訊息，則每一個欄位都要填..."
    else:
        post_form = forms.PostForm()
        #moods = models.Mood.objects.all()
        message = '如要張貼訊息，則每一個欄位都要填...'
    return render(request, 'blog/post2db.html', locals())

# 私人日記用
def diary_index(request):
    if 'username' in request.session:
        username = request.session['username']
        usercolor = request.session['usercolor']
    return render(request, 'diary/index.html', locals())

def diary_login(request):
    if request.method == 'POST':
        login_form = forms.DiaryLoginForm(request.POST)
        if login_form.is_valid():
            username=request.POST['user_name']
            usercolor=request.POST['user_color']
            message = '登入成功'
        else:
            message = '請檢察輸入的欄位內容'
    else:
        login_form = forms.DiaryLoginForm()
    try:
        if username:
            request.session['username'] = username
        if usercolor:
            request.session['usercolor'] = usercolor
    except:
        pass
    return render(request, 'diary/login.html', locals())

def diary_logout(request):
    request.session['username'] = None
    return redirect('/diary')