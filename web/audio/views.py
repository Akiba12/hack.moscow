from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from audio.models import data, services
import speechkit
import get_messages
import datetime


def main(request):
    if request.user.is_authenticated:
        service = services.objects.get(user=request.user)
        if (service.vk == "NULL") and (service.instagram == "NULL") and (service.telegram == "NULL") and (service.whatsapp == "NULL"):
            return redirect ('/addservice?reason={}'.format("noservices"))

        else:
            get_messages
            newfile = get_messages.newfile()
            if newfile != '':
                d = datetime.date()+'.opus'
                speechkit.recode(newfile, d)
                token = "AgAAAAAsHJhgAATuwWbeLLogYEKyh_JmCHj_evs"
                spchkt = speechkit.recognize(token)
                folder_id = "b1geohkpjn64hcd0bb7g"
                text = spchkt.recognize(d, folder_id)
                da = data()
                da.user = request.user
                da.service = 'telegram'
                da.message_id = newfile
                da.text = text
                da.sender = 'NULL'
                da.date = datetime.date()
                da.save()

            messages = data.objects.get(user=request.user)
            return render(request, 'mainAuth.html', {'username': request.user, 'messages': messages})


    else:
        if request.method == 'POST':
            if request.POST['button'] == 'Войти или Зарегестрироваться':
                user = request.POST['username']
                return redirect('/login?user={}'.format(user))


        elif request.method == 'GET':
            return render(request, "main.html", {})


        else:
            return HttpResponse("Unsupported request method {}".format(request.method))



def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        userlogin = request.GET['user']
        if User.objects.filter(username=userlogin).exists():
            return render(request, 'login.html', {'username': userlogin})
        else:
            return redirect('/register?user={}'.format(userlogin))

    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            messages.error(request, "Заполните все поля")

        # проверяем правильность логина и пароля
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/login?user=' + username)


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        userlogin = request.GET['user']
        return render(request, 'register.html', {'username': userlogin})


    if request.method == 'POST':
        username = request.POST.get('login', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if username == '' or password1 == '' or password2 == '':
            messages.error(request, 'Не все поля заполнены')
            return redirect('/register?user' + username)
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Ник уже занят')
            return redirect('/register?user=' + username)
        elif len(username) < 3:
            messages.error(request, 'Слишком короткий ник')
            return redirect('/register?user=' + username)
        elif len(username) > 20:
            messages.error(request, 'Слишком длинный ник')
            return redirect('/register?user=' + username)
        elif len(password1) < 6:
            messages.error(request, 'Слишком короткий пароль')
            return redirect('/register?user=' + username)
        elif len(password1) > 50:
            messages.error(request, 'Слишком длинный пароль')
            return redirect('/register?user=' + username)
        elif password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('/register?user=' + username)
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            login(request, user)
            service = services()

            service.user = request.user

            service.save()
            return redirect('/')


def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')


def addservice(request):
    if request.method == 'GET':
        if request.GET['reason'] == "noservices":
            text = "У вас не подключено ни одного сервиса, почему бы не добавить один?"

        return render(request, "addService.html", {'username': request.user, 'text': text})

def addTelegram(request):
    return render(request, "addTelegram.html", {'username': request.user})


def newaudio(filename):
    fileneme = filename




