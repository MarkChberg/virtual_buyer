
from django.conf.urls import url
from order import views

# Demo
#  url(r'^xxxx/',views.xxxx)
#  url(r'^xxxx/(\d+)',views.xxxx)
#  url(r'^xxxx/(?P<id>\d+)',views.xxxx)

urlpatterns = [
    url(r'^order_index/', views.order),
]