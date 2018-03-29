from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from pymysql import converters

#index
def index(req):
    ctx = {}
    c = connection.cursor()
    c.execute('select * from articles')
    ctx['articles'] = c.fetchall()
    return render(req, 'index.html', ctx)

@csrf_exempt
def articles(req):
    ctx = {}
    c = connection.cursor()
    c.execute('select * from articles')
    ctx['articles'] = c.fetchall()
    if req.is_ajax():
        # print(req.body)
        mdHTML = req.POST['mdHTML']
        c.execute('select count(*) from articles')
        nrows = c.fetchall()
        c.execute('insert into articles(id, content) values(%s, %s)', [1 + nrows[0][0], mdHTML])
    return render(req, 'articles.html', ctx)

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
