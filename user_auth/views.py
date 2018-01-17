# -*-coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django import forms
from .models import Users
# Create your views here.


def user_index(request):
    return render(request, 'user_auth/auth_index.html', {'content': '欢迎来到用户中心'})


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密 码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮 箱')
    phone = forms.IntegerField(label='手 机')


def regist(requst):
    if requst.method == 'POST':
        userform = UserForm(requst.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            phone = userform.cleaned_data['phone']

            try:
                registJudge = Users.objects.filter(username_text=username).get().username
                return render(requst, 'user_auth/regist.html', {'registJudge': registJudge})
            except:
                registAdd = Users.objects.create(username_text=username, password_text=password, user_emil=email, user_phone=phone)
                return render(requst, 'user_auth/regist.html', {'registAdd': registAdd, 'username': username})

    else:
        userform = UserForm()
    return render(requst, 'user_auth/regist.html', {'userform': userform})


def login(request):
    Method = request.method
    if Method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = Users.objects.filter(username_text__exact=username, password_text__exact=password )

            if user:
                return render(request, 'user_auth/auth_index.html', {'content': '欢迎来到用户中心'})
            else:
                return HttpResponse('用户名或密码错误，轻重新登录！')

    else:
        userform = UserForm()
    return render(request, 'user_auth/login.html', {'userform': userform})


def index(request):
    username = request.COOKIES.get('cookie_username', '')
    return render(request, 'user_auth/auth_index.html', {'username': username})


def logout(request):
    response = HttpResponse('logout!<br><a href="127.0.0.1:8000/regist>regist</a>"')
    response.delete_cookie('cookie_username')
    return response

