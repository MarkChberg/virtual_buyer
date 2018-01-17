from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

#def order(request):
#    return HttpResponse('欢迎来到订单中心')

#ORDER_LIST：全局订单变量，由search模块请求数据生成，付款后清空
ORDER_LIST = [
    {'product_id':'001','product_name':'2DS','price':'800','quantity':'1'},
    {'product_id':'002','product_name':'PS4','price':'2800','quantity':'1'}
]

def order(request):

    return render(request,'order/order_index.html',{'order_list':ORDER_LIST})

"""def quantity(request):
    if request.method == "POST":
        pass
    return render(request,'order_index.html',{'order_list':ORDER_LIST})"""

def order_confirm(request):
    if request.method == "POST":
        pass
    return render(request,'pay/pay_index.html',{'order_list':ORDER_LIST})