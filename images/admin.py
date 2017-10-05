# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'description',
        'location',
        'date'
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'image',
        'date'
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

     list_display = (
        'user',
        'comment',
        'image',
        'date'
    )   