"""Qsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from Qsite import settings
from Qapps import views,upload
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowMainPage,name="ShowMainPage"),
    path('signin/',views.signin,name="signin"),
    path('home/',views.home,name="home"),
    path('QA/',views.QA,name="QA"),
    path('HDNK/',views.HDNK,name="HDNK"),
    path('HSTB/',views.HSTB,name="HSTB"),
    path('CLB/',views.CLB,name="CLB"),
    path('QA/upload/',views.upload,name="upload"),
    path('QA/details/<str:q_id>/',views.details,name="details"),
    path('upload_save',upload.upload_save,name="upload_save"),
    path('reply_save/<str:q_id>',upload.reply_save,name="reply_save"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

