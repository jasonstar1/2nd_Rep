# 2nd_Rep
# coding=utf-8
import sys
import bottle, db, jinja2, time
from db import testdb, testdb1, Arg
from bottle import template, request, route, get, post, view


# urls = ("/favicon.ico", "dummy")


@route('/')
def home():
    return template('static/home.html')


@post('/sign_in')
def sign_in():
    use = request.POST["use"]
    psd = request.POST["psd"]
    use = Arg(use)
    psd = Arg(psd)
    sql = "select * from sign_in where use='%s'and psd='%s';" % (use, psd)
    rows = testdb1(sql)
    if rows==[]:
        return '<h5>用户名或密码错误！</h5>'
    else:
        return template('static/select.html')


# @post('/web/ajax_demo')
# def ajax_demo():
#     username = request.POST["user"]
#     return '''<div>
#         <p>hello: '''+username+'''！</p>
#     </div>'''


@post('/add')
def add():
    platenumber = request.POST["platenumber"]
    inorout = request.POST["inorout"]
    platenumber = Arg(platenumber)
    inorout = Arg(inorout)
    date_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
    sql = "insert into vehicle values('%s','%s','%s');" % (platenumber, inorout, date_time)
    rows = testdb(sql)
    return 'success!'


@post('/DeleteForm1')
def DeleteForm1():
    platenumber = request.POST["platenumber"]
    platenumber = Arg(platenumber)
    sql="Delete from vehicle where platenumber='%s';" % platenumber
    rows = testdb(sql)
    return '1'


@post('/web/SelectForm/')
@view('test.html')
def SelectForm():
    platenumber = request.POST["platenumber"]
    platenumber = Arg(platenumber)
    sql = "select * from vehicle where platenumber='%s';" % platenumber
    rows = testdb1(sql)
    if rows == []:
        return '<h5>车牌号码不正确！</h5>'
    global a, platenumber_list, inorout_list, date_time_list
    platenumber_list=[]
    inorout_list=[]
    date_time_list=[]
    a=0
    for row in rows:
        a+=1
        platenumber_list.append(row[0])
        inorout_list.append(row[1])
        date_time_list.append(row[2])
    info = {"a": a, "platenumber_list": platenumber_list, "inorout_list": inorout_list, "date_time_list": date_time_list}
    return info


@post('/SingleDel')
def SingleD():
    return ''


# @get('/myDiv/learnxml')
# def ajax_myDiv():
#     return 'hello world! <br/>I can use ajax now!'


# @post('/web/register/')
# def register():
#     platenumber = request.POST["platenumber"]
#     inorout = request.POST["inorout"]
#     date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     sql = "insert into vehicle values('%s','%s','%s');" % (platenumber, inorout, date_time)
#     rows = testdb(sql)
#     return '1'


# @post('/web/ajax_demo')
# def ajax_demo():
#     username = request.POST["user"]
#     return '''<div>
#         <p>hello: '''+username+'''！</p>
#     </div>'''


# @get('/form1')
# def form1():
#     return template('')


