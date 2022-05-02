from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import EXAM, QUESTION,OPTION

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
        context['questionsAndOptions'] =  {}

        for question in questions :
            
            context['questionsAndOptions'][question] = OPTION.objects.filter(question=question).values()
    
        return render(request,"Questions.html",context)

def submit_view(request):
    if request.method == "POST":
        examName = request.POST['examName']
        studentRollNumber = request.POST['studentRollNumber']
        return render(request,'submit.html')