from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import EXAM, QUESTION

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')


def check_exam_view(request):
    if request.method == "POST":
        examname = request.POST['examName']
        context = {}
        context['examName'] = examname
        try :
            exam  = EXAM.objects.get(name=examname )
            context['isexamexist'] = 'yes'

        except :
            context['isexamexist']= 'no'
        

        return render(request , 'index.html',context)


def question_view(request):
    if request.method == "POST":
        studentRollNumber = request.POST['studentRollNumber']
        examName = request.POST['examName']
    
        context = {}
        context['studentRollNumber'] = studentRollNumber
        context['examName'] = examName

        questions =  QUESTION.objects.filter(
            exam = EXAM.objects.get(name=examName )
        )
        context['questions'] = questions


    
        return render(request,"Questions.html",context)