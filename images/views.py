# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models

#request에서 들어온 id(image_id, request.user.id)와 image__id(model-DB에서 지정해준 아이디)가 같으면
#하트를 언하트 하는 기능.. 등

# image_id는 django에서 자동으로 만들어준다 -> 유저가 사진을 올리면, django가 알아서 image_id를 할당해주는 것

def like_image(request, image_id):

#Like 안의 객체인 image가 가지고 있는 id (객체안의 객체 개념)이므로 image__id라고 지정해줌

    #Like를 눌렀는데 이미 exist하고 있으면, 그것을 지워버림 (.delete())
    try:
        existing_like = models.Like.objects.get(
            image__id=image_id, user__id=request.user.id)
        existing_like.delete()
        response = HttpResponse(status=204)
    
    #Like를 눌렀는데 아직 exist하지 않으면, 다시 Like를 눌러버림 (.create())
    #Create할 때는 Like에다가 user, image에 관한 정보를 함께 붙여주어야 한다
    except models.Like.DoesNotExist:
        image = models.Image.objects.get(id=image_id)
        new_like = models.Like.objects.create(
            user=request.user,
            image=image)
        new_like.save()
        response = HttpResponse(status=200)

    return response

@csrf_exempt
def comment_image(request, image_id):
    
    comment= request.POST.get('comment', None)

    if comment is not None:

        image = models.Image.objects.get(id=image_id)
        input_comment = models.Comment.objects.create(
            comment=comment,
            user=request.user,
            image=image
            )

        input_comment.save()

        response = JsonResponse({
            'comment':input_comment.comment,
            'user':request.user.username
        })

    else:
        response = HttpResponse(status=406)
    
    return response