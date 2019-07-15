"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    # 后台主页
    url(r'^', views.index, name='index')

    # 登录
    # 退出
    # 浏览用户
    # 修改状态
    # 浏览分类
    # 添加类别
    # 修改类别
    # 添加商品
    # 浏览商品
    # 商品删除
    # 商品修改
    # 浏览订单
    # 处理订单
    # 订单详情
]
