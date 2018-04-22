from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from mysite.articleStruct import *

#index
def index(req):
    ctx = {}
    c = connection.cursor()
    c.execute('select * from articles')
    ctx['articles'] = c.fetchall()
    c.execute('select * from sider')
    ctx['sider'] = c.fetchall()
    return render(req, 'index.html', ctx)

@csrf_exempt
def articles(req):
    ctx = {}
    c = connection.cursor()
    c.execute('select * from articles order by time desc')
    Arts = []
    vec_art = c.fetchall()
    for it_art in vec_art:
        siderName = 'sider-art-%s' % it_art[0]
        c.execute('select * from `%s` order by time desc', siderName)
        vec_comm = c.fetchall()
        Comms = []
        for it_comm in vec_comm:
            Comms.append(Comm(it_comm[0], it_comm[1], it_comm[2], it_comm[3]))
        Arts.append(Art(it_art[0], it_art[1], Comms))
    ctx['Arts'] = Arts

    if req.is_ajax():
        # print(req.body)
        if req.POST.get('crateArt'):
            mdHTML = req.POST['mdHTML']
            timestamp = req.POST['timestamp']
            c.execute('insert into articles(time, content) values(%s, %s)', (timestamp, mdHTML))
            siderName = 'sider-art-%s' % timestamp
            c.execute('CREATE TABLE `%s` (  `time` VARCHAR(30) NOT NULL,  `content` VARCHAR(100) NOT NULL,  `link` VARCHAR(30) NOT NULL,  `author` VARCHAR(30) NOT NULL,  PRIMARY KEY (`time`))', siderName)

        if req.POST.get('delArt'):
            c.execute('DELETE FROM `articles` WHERE `time`=%s', req.POST['time'])
            siderName = 'sider-art-%s' % req.POST['time']
            c.execute('DROP TABLE `%s`', siderName)

        if req.POST.get('addComm'):
            time = req.POST['timestamp']
            link = req.POST['link']
            content = req.POST['content']
            author = req.POST['author']
            siderName = 'sider-art-%s' % link
            c.execute('insert into `%s` values(%s, %s, %s, %s)', (siderName, time, content, link, author))

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
