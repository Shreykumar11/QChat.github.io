from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('chatwin.html', views.chatwin, name='chatwin'),
    path('dchat.html', views.dchat, name='dchat'),
    path('home.html', views.home, name='home'),
    path('join.html', views.join, name='join'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]