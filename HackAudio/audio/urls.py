from django.urls import include, path
from audio.views import main, login_page, register, logout_page, addservice, addTelegram

urlpatterns = [
    path('', main),
    path('login', login_page),
    path('register', register),
    path('logout', logout_page),
    path('addservice', addservice),
    path('addservice/telegram/', addTelegram)
]