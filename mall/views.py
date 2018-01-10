# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.db import connection
import MySQLdb

from django.shortcuts import render

# Create your views here.

def index(request):
    return  HttpResponse("hello meini")

def all(request):
    with connection.cursor() as cursor:
        sql = 'select name, title,sales,price from mall_product'
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def one(request):
    """获取前端传进来的数据信息"""
    # 解析参数
    name = request.GET.get("name")
    # 拼接sql
    sql = "select name ,title,sales,price from mall_product WHERE name ='%s'" % (name)
    # 链接数据库
    db = MySQLdb.connect("localhost", "root", "mogujie2016", "mall")
    db.set_character_set('utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    # 获取返回数据
    data = dictfetchall(cursor)
    # 🈯️返回类型
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
# http://127.0.0.1:8000/add/?name=%E4%B8%8D%E6%AD%A3&sales=10&price=10&title=hello
def add(request):
    name = request.GET.get("name")
    sales = request.GET.get("sales")
    title = request.GET.get("title")
    price = request.GET.get("price")
    sql = "INSERT INTO mall_product(name, sales,title,price) \
               VALUES ( '%s', '%s','%s','%s')" % \
          (name, sales,title,price)
    db = MySQLdb.connect("localhost", "root", "mogujie2016", "mall")
    db.set_character_set('utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    return HttpResponse("SUCCESS")

def update(request):
    price = request.GET.get("price")
    name = request.GET.get("name")
    db = MySQLdb.connect("localhost", "root", "mogujie2016", "mall")
    db.set_character_set('utf8')
    cursor = db.cursor()
    sql = "UPDATE mall_product SET price = '%s' WHERE name = '%s'" % (price,name)
    cursor.execute(sql)
    db.commit()
    return HttpResponse("SUCCESS")


# 将返回结果转换成字典
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
