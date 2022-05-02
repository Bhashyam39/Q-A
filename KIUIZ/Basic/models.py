from datetime import date
from time import time
from urllib import response
from django.db import models
from django.utils import timezone
# Create your models here.


class EXAM(models.Model):
    """
    Here this a database table about exam/competetion.
    """
    name = models.CharField(max_length = 40, unique=True)
    about = models.TextField()
    conducted_by = models.TextField()
    is_open = models.BooleanField()



    def __str__(self):
        return self.name.upper()

class QUESTION(models.Model):
    query = models.TextField()
    exam = models.ForeignKey(EXAM,on_delete = models.CASCADE)

    def __str__(self):
        return self.query

class OPTION(models.Model):
    question = models.ForeignKey(QUESTION,on_delete = models.CASCADE)
    option = models.TextField()
    
    def __str__(self):
        return self.question

    def __str__(self):
        return self.option



class ANSWER(models.Model):
    question = models.ForeignKey(QUESTION,on_delete = models.CASCADE)
    solution = models.ForeignKey(OPTION,on_delete = models.CASCADE)




class RESPONSE(models.Model):
    exam                 = models.ForeignKey(EXAM,on_delete=models.CASCADE)
    studentRollNumber    = models.CharField(max_length=20)
    question             = models.ForeignKey(QUESTION,on_delete=models.CASCADE)
    response             = models.ForeignKey(OPTION,on_delete=models.CASCADE)
    date_time            = models.DateTimeField(auto_now_add=True,  )


