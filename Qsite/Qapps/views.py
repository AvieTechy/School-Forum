from django.shortcuts import render
from .models import Questions, Replys
# Create your views here.

def ShowMainPage(request):
    return render(request,"MainPage.html")

def signin(request):
    return render(request,"signin.html")

def home(request):
    return render(request,"home.html")

def QA(request):
    Ques = Questions.objects.all()
    return render(request,"QA.html",{"Ques":Ques})

def HSTB(request):
    return render(request,"HSTB.html")

def CLB(request):
    return render(request,"CLB.html")

def HDNK(request):
    return render(request,"HDNK.html")

def upload(request):
    return render(request,"upload.html")
def details(request,q_id):
    q = Questions.objects.filter(id=q_id).get()
    title = q.title
    text = q.text
    Ans = Replys.objects.filter(question=q).all()
    return render(request,"details.html",{'title':title,'text':text,'id':q_id,'Ans':Ans})