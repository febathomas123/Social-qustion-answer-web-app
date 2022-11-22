"""qaworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path,include
from . import views

urlpatterns = [

     path('', views.indez),
    path('login/', views.login),
    path('reg1/', views.reg1),
    path('reg2/', views.reg2),
    path('expert/', views.expert),
    path('logout/', views.logout),
    path('passwrd/', views.passwrd),
    path('user/', views.user1),
    path('answer/', views.answer),
    path('question_list/', views.question_list),
    path('user_added_questions/', views.user_added_questions),
    path('de_user_ques/<int:id>/', views.de_user_ques),
    path('user_req_ques/', views.user_req_ques),

    path('pending_question/', views.pending_question),
    path('pending/<int:id>', views.pending),
    path('qs_approve/<int:id>', views.qs_approve),
    path('approved_qs/', views.approved_qs),
    path('user_ans_ques/', views.user_ans_ques),
    path('de_pending/<int:id>', views.delete_pending_question),
    path('answering/<int:id>', views.answering),

    path('public_profile/', views.public_profile),
    path('public_eprofile/', views.public_eprofile),
    path('expert_profile/', views.expert_profile),
    path('expert_eprofile/', views.expert_eprofile),





]
