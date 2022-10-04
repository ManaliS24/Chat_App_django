from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register"),
    path('Change_pp/', views.change_pp, name="change_pp"),
    path('chat/', views.index, name="index"),
    path('friend/<str:pk>', views.detail, name="detail"),
    path('sent_msg/<str:pk>', views.sentMessages, name="sent_msg"),
    path('receive_msg/<str:pk>', views.receivedMessages, name="rec_msg"),
    path('notification/', views.chatNotification, name="notification"),
    path('received_last/', views.readLastMsg, name="rec_last"),
]