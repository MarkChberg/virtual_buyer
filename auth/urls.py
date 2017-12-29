
from django.conf.urls import url
from auth import views

# Demo
#  url(r'^xxxx/',views.xxxx)
#  url(r'^xxxx/(\d+)',views.xxxx)
#  url(r'^xxxx/(?P<id>\d+)',views.xxxx)

urlpatterns = [
    url(r'^auth_index/', views.auth_index),
]