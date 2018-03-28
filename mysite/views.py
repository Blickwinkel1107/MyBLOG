from django.shortcuts import render, redirect
from mysite.assembly import *
from django.shortcuts import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm



def index(req):
    ctx = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(req,user)
                req.session['username'] = username
                return  render(req, 'index.html', ctx)
            else:
                #比较失败，还在login
                ctx = {'isLogin': False,'pawd':False}
                return render(req, 'index.html', ctx)
    else:
        ctx = {'isLogin': False,'pswd':True}
    return render(req, 'index.html', ctx)



# 主页
# def index(req):
#     ctx = {}
#     ctx.update({'modals': modals})
#     if req.POST:
#         if req.POST['Lusername'] == req.POST['Lpassword']:
#             print('YES!!!!')
#         else:
#             print('NO~~~~~')
#     return render(req, 'index.html', ctx)

#
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
