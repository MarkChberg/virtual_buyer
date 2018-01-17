
from django.conf.urls import url
from user_auth import views

# Demo
#  url(r'^xxxx/',views.xxxx)
#  url(r'^xxxx/(\d+)',views.xxxx)
#  url(r'^xxxx/(?P<id>\d+)',views.xxxx)

urlpatterns = [
    url(r'^user_index/', views.user_index),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
]