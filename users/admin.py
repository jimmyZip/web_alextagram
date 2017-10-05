# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

#users라는 앱의 admin 파일에서 register를 해주어야 admin page상에서 나타남
#@은 decorator기능, model에서 
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass