from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Questions, Replys
from django.views.decorators.csrf import csrf_exempt

def upload_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("title-ques")
        username = request.POST.get("username")
        ques = request.POST.get("ques")
        tag = request.POST.get("tag")
        Question = Questions(title=title, text=ques, author=username, tag=tag)
        Question.save()
        messages.success(request, "Đã đăng Câu hỏi của bạn!")
        return HttpResponseRedirect(reverse("QA"))

def reply_save(request,q_id):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name = request.POST.get("name")
        ans = request.POST.get("ans")
        q = Questions.objects.filter(id=q_id).get()
        Rep = Replys(question=q, rep=ans, author_rep=name)
        Rep.save()
        messages.success(request, "Đã đăng Câu hỏi của bạn!")
        return HttpResponseRedirect(reverse("details", kwargs={'q_id':q_id}))
