from datetime import datetime
from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

class Question(models.Model):
    question = models.CharField(max_length=300,null=False,blank=False)
    question_arabic = models.CharField(max_length=300,null=False,blank=False)
    photo = models.ImageField(blank=True,null=True,upload_to="images/")
    A = models.CharField(max_length=200,null=False,blank=False)
    A_arabic = models.CharField(max_length=200,null=False,blank=False)
    B = models.CharField(max_length=200,null=False,blank=False)
    B_arabic = models.CharField(max_length=200,null=False,blank=False)
    C = models.CharField(max_length=200,null=False,blank=False)
    C_arabic = models.CharField(max_length=200,null=False,blank=False)
    D = models.CharField(max_length=200,null=False,blank=False)
    D_arabic = models.CharField(max_length=200,null=False,blank=False)
    t_answer = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.question

class Exam(models.Model):
    user_id = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user_id.username

class Answers(models.Model):
    exam_id = models.ForeignKey(Exam,null=False,blank=False,on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question,null=False,blank=False,on_delete=models.PROTECT)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer



class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tc = models.CharField(max_length=11,null=True,blank=True,unique=True)
    tel = models.CharField(max_length=11,blank=True,null=True)
    expire = models.DateTimeField(blank=True,default=datetime.now)
    def __str__(self):
        return str(self.user.first_name) +" "+ str(self.user.last_name)



class SlideShow(models.Model):
    slide_id = models.IntegerField(primary_key=True,null=False, blank=False)
    slideshow = models.ImageField(upload_to='img/slide/',null=False, blank=False)
    def __str__(self):
        return str(self.slide_id)

