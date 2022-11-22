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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('login/', include('app1.urls')),
    path('reg1/', include('app1.urls')),
    path('reg2/', include('app1.urls')),


    path('expert/', include('app1.urls')),
    path('passwrd/', include('app1.urls')),
    path('answer/', include('app1.urls')),



    path('question_list/', include('app1.urls')),
    path('approved_qs/', include('app1.urls')),
    path('pending_question/', include('app1.urls')),
    path('pending/<int:id>/', include('app1.urls')),
    path('qs_approve/<int:id>/', include('app1.urls')),
    path('de_pending/<int:id>/', include('app1.urls')),
    path('user_added_questions/', include('app1.urls')),
    path('de_user_ques/<int:id>/', include('app1.urls')),
    path('user_ans_ques/', include('app1.urls')),
    path('answering/<int:id>/', include('app1.urls')),
    path('user_req_ques/', include('app1.urls')),

    path('user/', include('app1.urls')),
    path('public_profile/', include('app1.urls')),
    path('public_eprofile/', include('app1.urls')),
    path('expert_profile/', include('app1.urls')),
    path('expert_eprofile/', include('app1.urls')),

    path('logout/', include('app1.urls')),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
