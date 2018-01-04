from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def man_index(request):
    return render(request, "man/man_index.html", {'content':'欢迎来到管理页面'})


def index(request):
    return render(request, 'index.html')
