"""virtual_buyer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from man import views as man_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^man/', include('man.urls')),
    url(r'^pay/', include('pay.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^user_auth/', include('user_auth.urls')),
    url(r'$', man_view.index)
]
