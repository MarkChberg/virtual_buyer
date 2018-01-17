from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

#def order(request):
#    return HttpResponse('欢迎来到订单中心')

#ORDER_LIST：全局订单变量，由search模块请求数据生成，付款后清空

'''
这个之后是数据库里找到的数据，如果模拟，可以看一下search那里的数据库文档，名字最好改成product_list
'''
ORDER_LIST = [
    {'product_id':'001','product_name':'2DS','price':'800','quantity':'1'},
    {'product_id':'002','product_name':'PS4','price':'2800','quantity':'1'}
]

'''每个方法前最好加上这个方法是干嘛用的注释'''
def order(request):

    return render(request,'order/order_index.html',{'order_list' : ORDER_LIST})

"""def quantity(request):
    if request.method == "POST":
        pass
    return render(request,'order_index.html',{'order_list':ORDER_LIST})"""

def order_confirm(request):
    if request.method == "POST":
        pass
    '''
    发起这个请求时，如果要跳转到自己开发的页面，不要用pay下的，用order下的，以免冲突
    '''
    return render(request,'pay/pay_index.html',{'order_list':ORDER_LIST})