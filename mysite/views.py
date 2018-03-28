from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# 第四个是 auth中用户权限有关的类。auth可以设置每个用户的权限。



#index
def index(req):
    return render(req, 'index.html')

def hello(req):
    #return HttpResponse("hello world!")
    ctx = {'hello': 'Hello Django!'}
    return render(req, "hello.html", ctx)

def calc(req):
    return render(req, 'calc.html')

# POST回传测试
def calc_post(req):
    ctx = {}
    if req.POST:
        ops = req.POST['ops']
        a = int(req.POST['input1'])
        b = int(req.POST['input2'])
        if ops == '+':
            c = a + b
        elif ops == '-':
            c = a - b
        elif ops == '*':
            c = a * b
        else:
            c = a / b
        ctx['res'] = c
        return render(req, "calc-post.html", ctx)
    else:
        return render(req, "calc-post.html", ctx)
