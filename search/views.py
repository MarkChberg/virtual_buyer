from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def search_index(request):
    return render(request, 'search/search.html', {'content':'欢迎来到搜索中心'})
