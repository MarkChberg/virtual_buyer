
from django.conf.urls import url
from order import views

# Demo
#  url(r'^xxxx/',views.xxxx)
#  url(r'^xxxx/(\d+)',views.xxxx)
#  url(r'^xxxx/(?P<id>\d+)',views.xxxx)



'''一个方法或按钮对应一个url，没有映射，功能无法实现 '''
urlpatterns = [
    url(r'^order_index/', views.order),
]