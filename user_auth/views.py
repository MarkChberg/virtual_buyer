from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def user_index(request) :
    return render(request, 'auth/auth_index.html', {'content': '欢迎来到用户中心'})
