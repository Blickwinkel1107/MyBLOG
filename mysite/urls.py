"""mysite URL Configuration

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
from django.urls import path
from mysite import views
from django.conf.urls import url
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^hello$', views.hello),
    url(r'^calc$', views.calc),
    url(r'^calc-post$', views.calc_post),
    url(r'^index$', views.index),
    url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^users/', include('users.urls')),
    # 将 auth 应用中的 urls 模块包含进来
    url(r'^users/', include('django.contrib.auth.urls')),
]
