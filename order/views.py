from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def order_index(request):
    return render(request, 'order/order_index.html', {'content':'欢迎来到订单中心'})