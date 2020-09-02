from django.db import models
from django.utils import timezone

class Student(models.Model):
	GENDER = [
		('male','Male'),
		('female','Female')
	]
	reg_no = models.CharField(max_length=100, unique=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	gender = models.CharField(max_length=10, choices=GENDER, default='male')
	date_of_birth = models.DateField(default=timezone.now)
	date_of_admission = models.DateField(default=timezone.now)
	mobile = models.CharField(max_length=10,unique=True)
	address = models.TextField(blank=True)

class OnlineClass(models.Model):
	std = models.CharField(max_length=5)
	teacher_name = models.CharField(max_length=20)
	c_date = models.DateField(default=timezone.now)
	cs_time = models.TimeField(auto_now=False,auto_now_add=False,null=True)
	ce_time = models.TimeField(auto_now=False,auto_now_add=False,null=True)
	c_day = models.CharField(max_length=5,blank=True)
	sub = models.CharField(max_length=10)
	c_link = models.URLField(max_length=200,blank=True)

class OnlineTest(models.Model):
	std = models.CharField(max_length=2)
	t_date = models.DateField(default=timezone.now)
	ts_time = models.TimeField(auto_now=False,auto_now_add=False,null=True)
	te_time = models.TimeField(auto_now=False,auto_now_add=False,null=True)
	t_day = models.CharField(max_length=5,blank=True)
	sub = models.CharField(max_length=10)
	t_link = models.URLField(max_length=200,blank=True)