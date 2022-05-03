from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import EXAM, QUESTION,OPTION , RESPONSE
import sys

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
        questions =  QUESTION.objects.filter(
            exam = EXAM.objects.get(name=examName)
        )
        
        for question in questions :
            response = request.POST[question.query]
            new = RESPONSE(
                exam                = EXAM.objects.get(name =   examName),
                studentRollNumber   = studentRollNumber,
                question            = question,
                response              = OPTION.objects.get( option= response),
            )
            new.save()
            

        return render(request,'submit.html')

def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    res = render(request,'code.html',{"code":code_part,"input":y,"output":output})
    return res

def greetings(request):
    res = render(request,'code.html')
    return res

def submit(request):
    res = render(request,'submit.html')
    return res