from django.db import models

# Create your models here.


class EXAM(models.Model):
    """
    Here this a database table about exam/competetion.
    """
    name = models.CharField(max_length = 40, unique=True)
    about = models.TextField()
    conducted_by = models.TextField()
    is_open = models.BooleanField()


class QUESTION(models.Model):
    query = models.TextField()
    exam = models.ForeignKey(EXAM,on_delete = models.CASCADE)

class OPTION(models.Model):
    question = models.ForeignKey(QUESTION,on_delete = models.CASCADE)
    option = models.TextField()


class ANSWER(models.Model):
    question = models.ForeignKey(QUESTION,on_delete = models.CASCADE)
    solution = models.ForeignKey(OPTION,on_delete = models.CASCADE)


class RESPONSE(models.Model):
    pass


