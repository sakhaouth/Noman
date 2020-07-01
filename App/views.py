import json

from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now

from .forms import MyForm
from .forms import SignIn
# Create your views here
from .models import MyData


def index(request):
    return render(request, 'App/index.html')


def checkSignIn(request):
    response = render(request, 'App/welcome.html')
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            if MyData.objects.filter(email=form.cleaned_data['email'], password=form.cleaned_data['password']):
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                # response.set_cookie('email',email,max_age=50)
                # response.set_cookie('password',password,max_age=50)
                request.session['email'] = email
                request.session['password'] = password
                return response
        else:
            return HttpResponse(response)
    else:
        return HttpResponse(response)
    return HttpResponse(response)


def signIn(request):
    if request.session.has_key('email') and request.session.has_key('password'):
        return render(request, 'App/welcome.html')
    response = render(request, 'App/signIn.html')
    return response


def setToDatabase(request):
    response = 'method'
    if request.method == "POST":
        response = 'invalid'
        form = MyForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['email']
            if MyData.objects.filter(email=mail):
                response = 'already'
                print("yes")
            else:
                name = form.cleaned_data['name']
                password = form.cleaned_data['password']
                date = now()
                code = 123
                response = 'new'
                database = MyData(name=name, email=mail, password=password, verification_code=code, date=date)
                database.save()
                cursor = connection.cursor()
                temp = str(mail)
                temp = temp.split('@')
                tableName = temp[0] + temp[1]
                tableName = tableName.split('.')
                tableName = tableName[0]
                query = 'CREATE TABLE {}(eventName varchar(255))'
                # return HttpResponse(query.format(tableName))
                # print(tableName)
                cursor.execute(query.format(tableName))
                return render(request,'App/signIn.html')
        else:
            print("Data is invalid")
    else:
        print("access is preserved")
    return HttpResponse(response)


def signup(request):
    response = render(request, 'App/hi.html')
    return response


def eventName(request):
    cursor = connection.cursor()
    temp = str(request.session['email'])
    temp = temp.split('@')
    tableName = temp[0] + temp[1]
    tableName = tableName.split('.')
    tableName = tableName[0]

    cursor.execute("SELECT eventName FROM " + tableName)
    row = cursor.fetchall()
    # data = list()
    # for x in row:
    #     data.append(x)
    json.dumps(row)
    # print('nn')
    # data = 10
    return JsonResponse(row, safe=False)


def ajx(request):
    data = dict()
    # data = [
    #     {
    #         'name': "Noman",
    #         'age': 25
    #     }
    # ]
    # s = {
    #     'name' : 'salman',
    #     'age' : 16
    # }
    # data.append(s)
    json.dumps(data)
    return JsonResponse(data, safe=False)


def function(request):
    cursor = connection.cursor()
    temp = str(request.session['email'])
    temp = temp.split('@')
    tableName = temp[0] + temp[1]
    tableName = tableName.split('.')
    tableName = tableName[0]
    query = 'CREATE TABLE {}(eventName varchar(255))'
    # return HttpResponse(query.format(tableName))
    # print(tableName)
    cursor.execute(query.format(tableName))
    return HttpResponse(tableName)


def logout(request):
    del request.session['email']
    del request.session['password']
    return HttpResponse('ok')


def add(request):
    if request.method == "GET":
        cursor = connection.cursor()
        temp = str(request.session['email'])
        temp = temp.split('@')
        tableName = temp[0] + temp[1]
        tableName = tableName.split('.')
        tableName = tableName[0]
        query = 'INSERT INTO ' + tableName + '(eventName) VALUES ("{}")'
        # values = "\"{}\""
        # values =
        cursor.execute(query.format(request.GET['name']))
        return HttpResponse('ok')


def hel(request):
    return HttpResponse('ddd')


def remove(request):
    if request.method == "GET":
        cursor = connection.cursor()
        temp = str(request.session['email'])
        temp = temp.split('@')
        tableName = temp[0] + temp[1]
        tableName = tableName.split('.')
        tableName = tableName[0]
        query = 'DELETE FROM '+tableName+' WHERE eventName = "{}"'
        # values = "\"{}\""
        # values =
        cursor.execute(query.format(request.GET['name']))
        # row = cursor.fetchall()
        return HttpResponse("ok")
