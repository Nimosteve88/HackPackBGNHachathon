from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('chatbox/', views.chatbot, name='chatbot'),
    path('login/',views.login, name='login'),
    path('pronouncequiz/',views.pronouncequiz, name='pronounce')

] 