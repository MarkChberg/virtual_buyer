from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def pay_index(request):
    return render(request, 'pay/pay_index.html', {'content':'欢迎来到支付中心'})