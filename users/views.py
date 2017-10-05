# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#render 라이브러리는 html template을 보여주는 기능을 함
from django.shortcuts import render

#View를 통해서 클라이언트 사이드와 통신하기 위한 라이브러리 import
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from images import models as image_models

#views.py에서 index함수를 정의해줘서 url request가 나왔을 때 함수에서 정의한 것을 출력하도록 한다
def index(request):
    if request.user.is_authenticated():
        images = image_models.Image.objects.all()
        context = {
            'images' : images
        }
        return render(request, 'feed.html', context)
    else:
        return render(request, 'login.html')

def login(request):
    if not request.user.is_authenticated():
        return render(request, "login.html")
    else:
        return render(request, "explore.html")

def explore(request):
    if request.user.is_authenticated():
        users = models.User.objects.exclude(id=request.user.id)
        #filter, exlude 를 사용해서 추출하거나 제외할 것을 선정하여 출력
        context = {
            'users':users
        }
        return render(request, "explore.html", context)
    else:
        return render(request, "login.html")

def profile(request, username_from_url):
    if request.user.is_authenticated():
        profile_user = models.User.objects.get(username=username_from_url)
        context = {
            'profile_user' : profile_user
        }
        return render(request, 'profile.html', context)
    else:
        return render(request, "login.html")