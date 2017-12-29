from django.contrib import admin
from django.conf.urls import url
from man import views

# Demo
#  url(r'^xxxx/',views.xxxx)
#  url(r'^xxxx/(\d+)',views.xxxx)
#  url(r'^xxxx/(?P<id>\d+)',views.xxxx)

urlpatterns = [
    url(r'^man_index/', views.man_index),
]