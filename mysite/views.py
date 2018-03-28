from django.shortcuts import render
from mysite.assembly import *
from django.shortcuts import HttpResponse


# 主页
def index(req):
    ctx = {}
    ctx.update({'modals': modals})
    return render(req, 'index.html', ctx)

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
